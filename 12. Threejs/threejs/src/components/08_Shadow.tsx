import * as THREE from "three";

import { useEffect, useRef } from "react";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";

import { RectAreaLightUniformsLib } from "three/examples/jsm/lights/RectAreaLightUniformsLib.js";
import { RectAreaLightHelper } from "three/examples/jsm/helpers/RectAreaLightHelper.js";

const Shadow = () => {
  const divContainer = useRef<HTMLDivElement>(null);
  const renderer = useRef<THREE.WebGLRenderer | null>(null);
  const scene = useRef<THREE.Scene | null>(null);
  const camera = useRef<THREE.PerspectiveCamera | null>(null);

  // const lightRef = useRef<THREE.DirectionalLight | null >(null)
  // const lighthelperRef = useRef<THREE.DirectionalLightHelper | null>(null)
  // const lightRef = useRef<THREE.PointLight | null >(null)
  // const lighthelperRef = useRef<THREE.PointLightHelper | null>(null)
  const lightRef = useRef<THREE.SpotLight | null >(null)
  const lighthelperRef = useRef<THREE.SpotLightHelper | null>(null)


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

    const auxLight = new THREE.DirectionalLight(0xffffff, 0.5);
    auxLight.position.set(0, 5, 0);
    auxLight.target.position.set(0, 0, 0);
    scene.current?.add(auxLight.target);
    scene.current?.add(auxLight);

    // //1. DirectionalLight 빛의 색상은 흰색, 빛의 세기는 1
    // const light = new THREE.DirectionalLight(0xffffff, 0.5);
    // light.position.set(0, 5, 0);
    // light.target.position.set(0, 0, 0);
    // scene.current?.add(light.target);
    // // 절두체 넓히기
    // light.shadow.camera.top = light.shadow.camera.right = 6;
    // light.shadow.camera.bottom = light.shadow.camera.left = -6;

    // //2. PointLight 빛의 색상은 흰색, 빛의 세기는 1
    // const light = new THREE.PointLight(0xffffff, 0.7);
    // light.position.set(0, 5, 0);

    //3. SpotLight
    const light = new THREE.SpotLight(0xffffff, 1);
    light.position.set(0, 5, 0);
    light.target.position.set(0, 0, 0);
    light.angle = THREE.MathUtils.degToRad(30);
    light.penumbra = 0.2;
    scene.current?.add(light.target);
  
    // 그림자 품질향상
    light.shadow.mapSize.width = light.shadow.mapSize.height = 2048;

    // 그림자의 외곽을 블러링
    light.shadow.radius = 5;

    scene.current?.add(light);
    lightRef.current = light

    const cameraHelper = new THREE.CameraHelper(light.shadow.camera);
    scene.current?.add(cameraHelper);

    // 그림자 여부
    light.castShadow = true;
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
    // 그림자 표현여부 
    ground.receiveShadow = true;
   
    scene.current?.add(ground);

    // BigSphereGeometry
    // const bigSphereGeometry = new THREE.SphereGeometry(1.5, 64, 64, 0, Math.PI);
    const bigSphereGeometry = new THREE.TorusKnotGeometry(1, 0.3, 128, 64, 2, 3);
    const bigSphereMaterial = new THREE.MeshStandardMaterial({
      color: "#ffffff",
      roughness: 0.1,
      metalness: 0.2,
    });
    const bigSphere = new THREE.Mesh(bigSphereGeometry, bigSphereMaterial);
    // bigSphere.rotation.x = THREE.MathUtils.degToRad(-90);
    bigSphere.position.y = 1.6;
    // 그림자 표현여부 
    bigSphere.receiveShadow = true;   // 그림자 받기
    bigSphere.castShadow = true;      // 그림자 주기

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
      // 그림자 표현여부 
      torus.receiveShadow = true;   // 그림자 받기
      torus.castShadow = true;      // 그림자 주기

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
    // 그림자 표현여부 
    smallSphere.receiveShadow = true;   // 그림자 받기
    smallSphere.castShadow = true;      // 그림자 주기

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

      // //1. DirectionalLight 광원이 작은 구를 추적함
      // if (lightRef.current?.target) {
      //   const smallSphere = smallSpherePibot.children[0];
      //   smallSphere.getWorldPosition(lightRef.current.target.position);

      //   // 헬퍼도 지속적으로 업데이트
      //   if(lighthelperRef) lighthelperRef.current?.update();
      // }

      // //2. PointLight 광원이 작은 구를 추적함
      // if (lightRef.current) {
      //   const smallSphere = smallSpherePibot.children[0];
      //   smallSphere.getWorldPosition(lightRef.current.position);

      //   // 헬퍼도 지속적으로 업데이트
      //   if(lighthelperRef) lighthelperRef.current?.update();
      // }

      //3. SpotLight 광원이 작은 구를 추적함
      if (lightRef.current?.target) {
        const smallSphere = smallSpherePibot.children[0];
        smallSphere.getWorldPosition(lightRef.current.target.position);

        // 헬퍼도 지속적으로 업데이트
        if(lighthelperRef) lighthelperRef.current?.update();
      }


    }
  };

  useEffect(() => {
    if (divContainer.current) {
      const ren = new THREE.WebGLRenderer({ antialias: true });
      ren.setPixelRatio(window.devicePixelRatio);
      divContainer.current.appendChild(ren.domElement);
      //그림자 활성화
      ren.shadowMap.enabled = true;

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

export default Shadow;