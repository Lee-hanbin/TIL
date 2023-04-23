import * as THREE from "three";

import { useEffect, useRef } from "react";
import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";

import { RectAreaLightUniformsLib } from "three/examples/jsm/lights/RectAreaLightUniformsLib.js";
import { RectAreaLightHelper } from "three/examples/jsm/helpers/RectAreaLightHelper.js";

const Camera = () => {
  const divContainer = useRef<HTMLDivElement>(null);
  const renderer = useRef<THREE.WebGLRenderer | null>(null);
  const scene = useRef<THREE.Scene | null>(null);
  const camera = useRef<THREE.OrthographicCamera | THREE.PerspectiveCamera | null>(null);

  const lightRef = useRef<THREE.RectAreaLight | null >(null)
  const lighthelperRef = useRef<RectAreaLightHelper | null>(null)
  const controls = useRef<OrbitControls |null>(null);


  /** 카메라 커스텀 함수 */
  const SetupCamera = () => {

    //1. PerspectiveCamera
    const cam = new THREE.PerspectiveCamera(
      75, //fovy ( 단위는 radian 아니고 degree )
      window.innerWidth / window.innerHeight, //aspect 
      0.1, //zNear
      100  //zFar
    );
    
    // //2. OrthographicCamera
    // const aspect = window.innerWidth / window.innerHeight;
    // const cam = new THREE.OrthographicCamera(
    //   -1*aspect, 1*aspect,  //xLeft, xRight
    //   1, -1,    //yTop, yBottom
    //   0.1, 100  //zNear, zFar 
    // )
    
    // cam.zoom = 0.15;

    // cam.position.z = 2;
    // 카메라 위치 조정
    cam.position.set(7,7,0);      // 카메라의 위치는 7, 7, 0
    cam.lookAt(0, 0, 0);          // 카메라가 바라보는 곳이 0, 0, 0

    camera.current = cam;
  };

  /** 조명 커스텀 함수 */
  const SetupLight = () => {
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


    // 작은 공을 추적하기 위해 객체를 만듦 ( 작은 구가 바라보는 화면을 카메라로 전환하기 위해 )
    const targetPivot = new THREE.Object3D();
    const target = new THREE.Object3D();  // Mesh 대신에 Object3D이므로 화면상에 보이지는 않음
    targetPivot.add(target);
    targetPivot.name = "targetPivot";
    target.position.set(3, 0.5, 0);
    scene.current?.add(targetPivot);

  };

  /** 렌더링 될 때마다 사이즈 초기화 */
  const resize = () => {
    const width = divContainer.current?.clientWidth || 0;
    const height = divContainer.current?.clientHeight || 0;
    const aspect = width / height;

    // if (camera.current !== null) {
    //   camera.current.aspect = width / height;
    //   camera.current.updateProjectionMatrix();
    // }
    // renderer.current?.setSize(width, height);

    if (camera.current instanceof THREE.PerspectiveCamera) {
      camera.current.aspect = aspect;
    } else if ( camera.current instanceof THREE.OrthographicCamera ){
      camera.current.left = -1 * aspect;
      camera.current.right = 1 * aspect;
    }

    camera.current?.updateProjectionMatrix();

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
      

      // 카메라가 작은 구를 추적함 ( 작은 구가 바라보는 화면을 카메라로 전환하기 위해 )
      const smallSphere = smallSpherePibot.children[0];
      if (camera.current !== null ) {
        smallSphere.getWorldPosition(camera.current.position);
      }
      // 작은 구보다 10도 더 회전시켜서 작은 구의 방향을 잡음
      const targetPivot = scene.current?.getObjectByName("targetPivot");
      if(targetPivot){
        targetPivot.rotation.y = THREE.MathUtils.degToRad(time*50 + 10);

        const target = targetPivot.children[0];
        const pt = new THREE.Vector3();

        // target을 카메라가 잡게 함
        target.getWorldPosition(pt);
        camera.current?.lookAt(pt);
      }
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

export default Camera;