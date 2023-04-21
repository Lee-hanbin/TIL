import * as THREE from "three";

import { useEffect, useRef } from "react";

import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import circle from "../assets/lowpoly/circle.png"

const Material = () => {
  const divContainer = useRef<HTMLDivElement>(null);
  const renderer = useRef<THREE.WebGLRenderer | null>(null);
  const scene = useRef<THREE.Scene | null>(null);
  const camera = useRef<THREE.PerspectiveCamera | null>(null);

  // const pointsMaterial = useRef<THREE.Points | null>(null);
  const lineMaterial = useRef<THREE.Line | null>(null);

  const controls = useRef<OrbitControls |null>(null);

  /** 카메라 커스텀 함수 */
  const SetupCamera = () => {
    const width = divContainer.current?.clientWidth || 0;
    const height = divContainer.current?.clientHeight || 0;
    const cam = new THREE.PerspectiveCamera(75, width / height, 0.1, 100);
    cam.position.z = 7;
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
    const vertices = [
      -1, 1, 0,
       1, 1, 0,
      -1,-1, 0,
       1,-1, 0,
    ];

    const geometry = new THREE.BufferGeometry();
    geometry.setAttribute(
      "position",
      new THREE.Float32BufferAttribute(vertices, 3)
    );
    
    // // 선에 대한 색상을 지정
    // const material = new THREE.LineBasicMaterial({ color: 0xffff00 });

    // 라인의 대쉬를 지정! 대신 computeLineDistances를 지정해줘야 적용됨!
    const material = new THREE.LineDashedMaterial({
      color: 0xffff00,
      dashSize: 0.2,    // 선의 길이
      gapSize: 0.1,     // 빈 공간의 길이
      scale: 1          // 빈도수? 정의
    })

    const line = new THREE.Line(geometry, material);
    line.computeLineDistances();
    scene.current?.add(line)
    lineMaterial.current = line;

    // // 10000개의 좌표를 난수로 배열에 추가
    // const vertices = [];
    // for (let i = 0; i < 10000; i++) {
    //   const x = THREE.MathUtils.randFloatSpread(5);
    //   const y = THREE.MathUtils.randFloatSpread(5);
    //   const z = THREE.MathUtils.randFloatSpread(5);

    //   vertices.push(x, y, z);
    // }

    // const geometry = new THREE.BufferGeometry();
    // geometry.setAttribute(
    //   "position",
    //   new THREE.Float32BufferAttribute(vertices, 3)     // 3이 의미하는 건 x, y, z 라는 세개의 좌표
    // );
    
    // // 객체 하나하나의 모형을 조정할 수 있음
    // const sprite = new THREE.TextureLoader().load(circle)
    

    // const material = new THREE.PointsMaterial({
    //   map: sprite,
    //   alphaTest: 0.2,       // 객체가 alphaTest 값보다 클때만 픽셀이 렌더링 됨
    //   // color: 0xff0000,
    //   // color: "yellow",
    //   color: "#00ffff",
    //   size: 0.1,
    //   // sizeAttenuation: false
    //   sizeAttenuation: true     // true 하면 카메라 거리에 따라 크기가 달라진다.
    // });

    // const points = new THREE.Points(geometry, material);
    
    // scene.current?.add(points)
    // pointsMaterial.current = points;
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
  //   pointsMaterial.current!.rotation.x = time;
  //   pointsMaterial.current!.rotation.y = time;
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

export default Material;