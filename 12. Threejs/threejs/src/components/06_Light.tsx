import * as THREE from "three";

import { useEffect, useRef } from "react";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";

import { RectAreaLightUniformsLib } from "three/examples/jsm/lights/RectAreaLightUniformsLib.js";
import { RectAreaLightHelper } from "three/examples/jsm/helpers/RectAreaLightHelper.js";

const Light = () => {
  const divContainer = useRef<HTMLDivElement>(null);
  const renderer = useRef<THREE.WebGLRenderer | null>(null);
  const scene = useRef<THREE.Scene | null>(null);
  const camera = useRef<THREE.PerspectiveCamera | null>(null);

  // const lightRef = useRef<THREE.AmbientLight | null >(null)
  // const lightRef = useRef<THREE.HemisphereLight | null >(null)
  // const lightRef = useRef<THREE.DirectionalLight | null >(null)
  // const lighthelperRef = useRef<THREE.DirectionalLightHelper | null>(null)
  // const lightRef = useRef<THREE.PointLight | null >(null)
  // const lighthelperRef = useRef<THREE.PointLightHelper | null>(null)
  // const lightRef = useRef<THREE.SpotLight | null >(null)
  // const lighthelperRef = useRef<THREE.SpotLightHelper | null>(null)
  const lightRef = useRef<THREE.RectAreaLight | null >(null)
  const lighthelperRef = useRef<RectAreaLightHelper | null>(null)

  const controls = useRef<OrbitControls |null>(null);


  /** 카메라 커스텀 함수 */
  const SetupCamera = () => {
    const width = divContainer.current?.clientWidth || 0;
    const height = divContainer.current?.clientHeight || 0;
    const cam = new THREE.PerspectiveCamera(75, width / height, 0.1, 100);
    
    // cam.position.z = 2;
    // 카메라 위치 조정
    cam.position.set(7,7,0);      // 카메라의 위치는 7, 7, 0
    cam.lookAt(0, 0, 0);          // 카메라가 바라보는 곳이 0, 0, 0

    camera.current = cam;
  };

  /** 조명 커스텀 함수 */
  const SetupLight = () => {
    // //1. AmbientLight scene에 존재하는 모든 물체에 대해서 단일 색상으로 보여지게 함
    // const light = new THREE.AmbientLight(0xff0000, 0.2)

    // //2. HemisphereLight (위에서 비춰지는 색상, 아래서 비춰지는 색상, 빛의 세기)
    // const light = new THREE.HemisphereLight("#b0d8f5", "#bb7a1c", 1)

    // //3. DirectionalLight 빛의 색상은 흰색, 빛의 세기는 1
    // // 광원의 위치는 0, 5, 0
    // // 광원이 비치는 대상의 위치를 0, 0, 0
    // const light = new THREE.DirectionalLight(0xffffff, 1);
    // light.position.set(0, 5, 0);
    // light.target.position.set(0, 0, 0);
    // scene.current?.add(light.target);
    // // 조명의 위치와 조명이 가리키는 방향을 알려줌
    // const helper = new THREE.DirectionalLightHelper(light);
    // scene.current?.add(helper)
    // lighthelperRef.current = helper

    // //4. PointLight : 광원의 위치에서 사방으로 퍼져나감
    // const light = new THREE.PointLight(0xffffff, 2);
    // light.position.set(0, 5, 0);

    // light.distance = 10;

    // const helper = new THREE.PointLightHelper(light);
    // scene.current?.add(helper)
    // lighthelperRef.current = helper

    // //5. SpotLight : 광원의 위치에서 사방으로 퍼져나감
    // const light = new THREE.SpotLight(0xffffff, 1);
    // light.position.set(0, 5, 0);
    // light.target.position.set(0, 0, 0);
    // light.angle = THREE.MathUtils.degToRad(30);
    // light.penumbra = 1;
    // scene.current?.add(light.target)

    // const helper = new THREE.SpotLightHelper(light);
    // scene.current?.add(helper)
    // lighthelperRef.current = helper

    //6. RectAreaLight : 광원의 위치에서 사방으로 퍼져나감
    RectAreaLightUniformsLib.init(); 
    // 빛의 색상, 빛의 세기, 광원의 가로길이, 광원의 세로길이
    const light = new THREE.RectAreaLight(0xffffff, 10, 10, 5);
    light.position.set(0, 5, 0);
    light.rotation.x = THREE.MathUtils.degToRad(-90);

    const helper = new RectAreaLightHelper(light);
    scene.current?.add(helper)
    lighthelperRef.current = helper

    scene.current?.add(light);
    lightRef.current = light
  };

  /** 모델 커스텀 함수 */
  const SetupModel = () => {
    // ground
    const groundGeometry = new THREE.PlaneGeometry(10, 10);
    const groundMaterial = new THREE.MeshStandardMaterial({
      color: "#2c3e50",
      roughness: 0.5,
      metalness: 0.5,
      side: THREE.DoubleSide
    });

    const ground = new THREE.Mesh(groundGeometry, groundMaterial);
    ground.rotation.x = THREE.MathUtils.degToRad(-90);
    scene.current?.add(ground);

    // BigSphereGeometry
    const bigSphereGeometry = new THREE.SphereGeometry(1.5, 64, 64, 0, Math.PI);
    const bigSphereMaterial = new THREE.MeshStandardMaterial({
      color: "#ffffff",
      roughness: 0.1,
      metalness: 0.2,
    });
    const bigSphere = new THREE.Mesh(bigSphereGeometry, bigSphereMaterial);
    bigSphere.rotation.x = THREE.MathUtils.degToRad(-90);
    scene.current?.add(bigSphere);

    //Torus
    const torusGeometry = new THREE.TorusGeometry(0.4, 0.1, 32, 32);
    const torusMaterial = new THREE.MeshStandardMaterial({
      color: "#9b59b6",
      roughness: 0.5,
      metalness: 0.9,
    });

    for (let i=0; i<8; i++) {
      const torusPivot = new THREE.Object3D();
      const torus = new THREE.Mesh(torusGeometry, torusMaterial);
      torusPivot.rotation.y = THREE.MathUtils.degToRad(45 * i);
      torus.position.set(3, 0.5, 0);
      torusPivot.add(torus);
      scene.current?.add(torusPivot);
    }

    //SmallSphere
    const smallShphereGeometry = new THREE.SphereGeometry(0.3, 32, 32);
    const smallShphereMaterial = new THREE.MeshStandardMaterial({
      color: "#e74c3c",
      roughness: 0.2,
      metalness: 0.5
    });
    const smallSpherePivot = new THREE.Object3D();
    const smallSphere = new THREE.Mesh(smallShphereGeometry, smallShphereMaterial);
    smallSpherePivot.add(smallSphere);
    smallSpherePivot.name = "smallSpherePivot";
    smallSphere.position.set(3, 0.5, 0);
    scene.current?.add(smallSpherePivot);

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
    time *= 0.001;

    // 작은 구를 큰 반원을 기준으로 돌게 함
    const smallSpherePibot = scene.current?.getObjectByName("smallSpherePivot");
    if (smallSpherePibot) {
      smallSpherePibot.rotation.y = THREE.MathUtils.degToRad(time*50);

      // //3. DirectionalLight 광원이 작은 구를 추적함
      // if (lightRef.current?.target) {
      //   const smallSphere = smallSpherePibot.children[0];
      //   smallSphere.getWorldPosition(lightRef.current.target.position);

      //   // 헬퍼도 지속적으로 업데이트
      //   if(lighthelperRef) lighthelperRef.current?.update();
      // }

      // //4. PointLight 광원이 작은 구를 추적함
      // if (lightRef.current) {
      //   const smallSphere = smallSpherePibot.children[0];
      //   smallSphere.getWorldPosition(lightRef.current.position);

      //   // 헬퍼도 지속적으로 업데이트
      //   if(lighthelperRef) lighthelperRef.current?.update();
      // }

      // //5. SpotLight 광원이 작은 구를 추적함
      // if (lightRef.current?.target) {
      //   const smallSphere = smallSpherePibot.children[0];
      //   smallSphere.getWorldPosition(lightRef.current.target.position);

      //   // 헬퍼도 지속적으로 업데이트
      //   if(lighthelperRef) lighthelperRef.current?.update();
      // }


    }
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

export default Light;