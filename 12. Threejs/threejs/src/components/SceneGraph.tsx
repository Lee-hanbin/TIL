import * as THREE from "three";

import { useEffect, useRef } from "react";

const SceneGraph = () => {
  const divContainer = useRef<HTMLDivElement>(null);
  const renderer = useRef<THREE.WebGLRenderer | null>(null);
  const scene = useRef<THREE.Scene | null>(null);
  const camera = useRef<THREE.PerspectiveCamera | null>(null);
  const SoloarSystemObject = useRef<THREE.Object3D | null>(null);

  /** 카메라 커스텀 함수 */
  const SetupCamera = () => {
    const width = divContainer.current?.clientWidth || 0;
    const height = divContainer.current?.clientHeight || 0;
    const cam = new THREE.PerspectiveCamera(75, width / height, 0.1, 100);
    cam.position.z = 25;
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
    const solarSystem = new THREE.Object3D();
    scene.current?.add(solarSystem)

    const radius = 1;
    const widthSegment = 12;
    const heightSegment = 12;
    const sphereGeometry = new THREE.SphereGeometry(
      radius,
      widthSegment,
      heightSegment
    );

    const sunMeterial = new THREE.MeshPhongMaterial({
      emissive: 0xffff00,
      flatShading: true
    });

    const sunMesh = new THREE.Mesh(sphereGeometry, sunMeterial);
    sunMesh.scale.set(3, 3, 3);
    solarSystem.add(sunMesh);

    
    const earthOribit = new THREE.Object3D();
    solarSystem.add(earthOribit);

    const earthMaterial = new THREE.MeshPhongMaterial({
      color: 0x2233ff,
      emissive: 0x112244,
      flatShading: true
    });

    const earthMesh = new THREE.Mesh(sphereGeometry, earthMaterial);
    earthOribit.position.x = 10;
    earthOribit.add(earthMesh);

    const moonOrbit = new THREE.Object3D();
    moonOrbit.position.x = 2;
    earthOribit.add(moonOrbit);

    const moonMaterial = new THREE.MeshPhongMaterial({
      color: 0x888888,
      emissive: 0x222222,
      flatShading: true
    });

    const moonMesh = new THREE.Mesh(sphereGeometry, moonMaterial);
    moonMesh.scale.set(0.5, 0.5, 0.5);
    moonOrbit.add(moonMesh);
    
    SoloarSystemObject.current = solarSystem;
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

  const render = (time: number) => {
    renderer.current?.render(scene.current!, camera.current!);
    update(time);
    requestAnimationFrame(render);
  };

  const update = (time: number) => {
    time *= 0.001;
    // SoloarSystemObject.current!.rotation.x = time / 2;
    SoloarSystemObject.current!.rotation.y = time / 2;
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

export default SceneGraph;