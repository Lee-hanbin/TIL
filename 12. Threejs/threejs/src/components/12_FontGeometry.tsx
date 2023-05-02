import * as THREE from "three";

import { useEffect, useRef } from "react";

import { FontLoader } from "three/examples/jsm/loaders/FontLoader.js"
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import { TextGeometry } from "three/examples/jsm/geometries/TextGeometry.js"
import fontJSON from "../assets/font/NanumMyeongjo_Regular.json"

const FontGeometry = () => {
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
    const color = 0xffffff;
    const intensity = 1;
    const light = new THREE.DirectionalLight(color, intensity);
    light.position.set(-1, 2, 4);
    scene.current?.add(light);
  };

  /** 모델 커스텀 함수 */
  const SetupModel = () => {
    const loader = new FontLoader();
    const font = loader.parse(fontJSON);
    const geometry = new TextGeometry(
      "대한민국\nKorea #1",
      {
        font: font,
        size: 0.3,
        height: 0.2,
        curveSegments: 12,
        bevelEnabled: true,
        bevelThickness:  0.03,
        bevelSize: 0.03,
        bevelOffset: 0.005,
        bevelSegments: 24
      }
    );

    // // geometry에 대한 가로 세로 높이 계산
    // geometry.computeBoundingBox();
    // const minX = (geometry.boundingBox!.max.x - geometry.boundingBox!.min.x) / 2.0;
    // const minZ = (geometry.boundingBox!.max.z - geometry.boundingBox!.min.z) / 2.0;
    // // 중심 값만큼 geometry 중심을 이동
    // geometry.translate(-minX, 0, -minZ); 
    
    // 위의 4줄을 한줄로 표현 가능
    geometry.center();

    const material = new THREE.MeshStandardMaterial({
      color: "#689F38",
      roughness: 0.3,
      metalness: 0.7
    });

    let mesh = new THREE.Mesh(geometry, material);
    scene.current?.add(mesh);
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

export default FontGeometry;
