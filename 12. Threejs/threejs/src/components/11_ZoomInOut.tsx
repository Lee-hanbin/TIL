import * as THREE from "three";

import { useEffect, useRef } from "react";

import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js"
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import grayCar from "../assets/lowpoly/carGray.glb"
import greenCar from "../assets/lowpoly/carGoblin.glb"
import redCar from "../assets/lowpoly/carRed.glb"
import whiteCar from "../assets/lowpoly/carWhite.glb"

const ZoomInOut = () => {
  const divContainer = useRef<HTMLDivElement>(null);
  const renderer = useRef<THREE.WebGLRenderer | null>(null);
  const scene = useRef<THREE.Scene | null>(null);
  const camera = useRef<THREE.PerspectiveCamera | null>(null);

  const controls = useRef<OrbitControls |null>(null);

  /** 카메라 커스텀 함수 */
  const SetupCamera = () => {
    const width = divContainer.current?.clientWidth || 0;
    const height = divContainer.current?.clientHeight || 0;
    const cam = new THREE.PerspectiveCamera(75, width / height, 0.1, 100);
    cam.position.z = 2;
    camera.current = cam;
  };

  /** 조명 커스텀 함수 */
  const SetupLight = () => {
    const ambienttLight = new THREE.HemisphereLight(0xffffff, 0x444444, 0.4);
    scene.current?.add(ambienttLight);

    const color = 0xffffff;
    const intensity = 1.5;

    const light1 = new THREE.DirectionalLight(color, intensity);
    light1.position.set(-1, 2, 0);
    scene.current?.add(light1);

    const light2 = new THREE.DirectionalLight(color, intensity);
    light2.position.set(1, 4, 0);
    scene.current?.add(light2);
  };

  /** 모델 커스텀 함수 */
  const SetupModel = () => {
    const gltfLoader = new GLTFLoader();
    const items = [
      {url: whiteCar},
      {url: grayCar}
    ]

    items.forEach((item, index) => {
      gltfLoader.load(item.url, (glb) => {
        const obj3d = glb.scene;

        const box = new THREE.Box3().setFromObject(obj3d);
        const sizeBox = box.max.z - box.min.z;
        const scale = 1 / sizeBox;
        const tx = (index / (items.length-1)) - 0.5;
        obj3d.scale.set(scale, scale, scale);
        obj3d.position.set(tx, -box.min.y*scale, 0);

        scene.current?.add(obj3d);
        obj3d.name = "car"

        scene.current?.add(new THREE.BoxHelper(obj3d))
      })
    })

    const boxGeometry = new THREE.CylinderGeometry(1.2, 1.2, 0.1, 64);
    const boxMaterial = new THREE.MeshStandardMaterial({
      color: 0x454545,
      metalness: 0.5,
      roughness: 0.5
    });
    const box = new THREE.Mesh(boxGeometry, boxMaterial);

    box.position.set(0, -0.05, -0.3)
    scene.current?.add(box)
  };

  /** 렌더링 될 때마다 사이즈 초기화 */
  const resize = () => {
    const width = divContainer.current?.clientWidth || 0;
    const height = divContainer.current?.clientHeight || 0;

    if (camera.current !== null) {
      camera.current.aspect = width / height;
      camera.current.updateProjectionMatrix();
    }
    renderer.current?.setSize(width, height);
  };
  
  /** 마우스 그래그로 회전시킴 */
  const SetupControls = () => {
    if (camera.current) {
      controls.current = new OrbitControls(camera.current, divContainer.current!); // OrbitControls를 초기화합니다.
      controls.current.enableDamping = true;
    }
  }

  const render = (time: number) => {
    renderer.current?.render(scene.current!, camera.current!);
    update(time);
    requestAnimationFrame(render);
  };

  const update = (time: number) => {
    time *= 0.01;

  };

  useEffect(() => {
    if (divContainer.current) {
      const ren = new THREE.WebGLRenderer({ antialias: true });
      ren.setPixelRatio(window.devicePixelRatio);
      divContainer.current.appendChild(ren.domElement);
      ren.shadowMap.enabled = true;
      ren.shadowMap.type = THREE.PCFSoftShadowMap;
      renderer.current = ren;

      const scn = new THREE.Scene();
      scene.current = scn;

      SetupCamera();
      SetupLight();
      SetupModel();
      SetupControls();
      // scene.current.background = new THREE.Color("#0000");
      // let light =new THREE.DirectionalLight(0xffff00, 10);
      // scene.current.add(light)

      window.onresize = resize;
      resize();

      requestAnimationFrame(render);
    }
  }, []);

  return(
  <div
    style={{ backgroundColor: 'grey', width: '100%', height: 1000 }}
    ref={divContainer} 
  />
  )
};

export default ZoomInOut;