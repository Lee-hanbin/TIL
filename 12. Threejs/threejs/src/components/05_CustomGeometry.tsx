import * as THREE from "three";

import { useEffect, useRef } from "react";

import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import { VertexNormalsHelper } from "three/examples/jsm/helpers/VertexNormalsHelper.js"
import textureImg from "../assets/lowpoly/uv_grid_directx.png"

const CustomGeometry = () => {
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
    const rawPositions = [
      -1,-1, 0,
       1,-1, 0,
      -1, 1, 0,
       1, 1, 0,
    ];

    //법선 벡터 직접 지정 가능 
    // => 여기서 모두 0, 0, 1 인 이유는 메쉬의 정점들이 모두 xy 평면에 있기 때문
    const rawNarmals = [
      0, 0, 1,
      0, 0, 1,
      0, 0, 1,
      0, 0, 1,
    ]

    //color 속성을 이용해서 각 vertax 마다 색상 지정 가능
    const rawColor = [
      1, 0, 0,
      0, 1, 0,
      0, 0, 1,
      1, 1, 0
    ];

    //uv 속성 텍스쳐 맵핑을 위한 속성
    const rawUVs = [
      0, 0,
      1, 0,
      0, 1,
      1, 1
    ];


    // 맵핑 과정
    const positions = new Float32Array(rawPositions);
    const normals = new Float32Array(rawNarmals);
    const colors = new Float32Array(rawColor)
    const uvs = new Float32Array(rawUVs);

    const geometry = new THREE.BufferGeometry();


    // geometry에 속성 지정
    geometry.setAttribute("position", new THREE.BufferAttribute(positions, 3));
    geometry.setAttribute("normal", new THREE.BufferAttribute(normals, 3));
    geometry.setAttribute("color", new THREE.BufferAttribute(colors, 3));
    geometry.setAttribute("uv", new THREE.BufferAttribute(uvs, 2));

    geometry.setIndex([
      0, 1, 2,
      2, 1, 3
    ]);

    // 모든 정점에 대한 법선 벡터
    // geometry.computeVertexNormals();
    
    const textureLoader = new THREE.TextureLoader();
    const map = textureLoader.load(textureImg);

    // 이때, 각 vertex 별로 색상을 지정하려면 기본 mesh 색상을 흰색으로 해야함
    const material = new THREE.MeshPhongMaterial({ 
      color: 0xffffff, 
      vertexColors: true,
      map: map,
    });

    const box = new THREE.Mesh(geometry, material)
    scene.current?.add(box);

    //법선벡터 시각화
    const helper = new VertexNormalsHelper(box, 0.1, 0xffff00);
    scene.current?.add(helper);

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

export default CustomGeometry;