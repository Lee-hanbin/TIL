import * as THREE from "three";

import { useEffect, useRef } from "react";

import { GLTFLoader } from "three/examples/jsm/loaders/GLTFLoader.js"
import { OrbitControls } from 'three/examples/jsm/controls/OrbitControls';
import grayCar from "../assets/lowpoly/carGray.glb"
import greenCar from "../assets/lowpoly/carGoblin.glb"
import { gsap } from 'gsap';
import redCar from "../assets/lowpoly/carRed.glb"
import whiteCar from "../assets/lowpoly/carWhite.glb"

const ZoomInOut = () => {
  const divContainer = useRef<HTMLDivElement>(null);
  const renderer = useRef<THREE.WebGLRenderer | null>(null);
  const scene = useRef<THREE.Scene | null>(null);
  const camera = useRef<THREE.PerspectiveCamera | null>(null);
  const controls = useRef<OrbitControls |null>(null);

  const raycasterRef = useRef<THREE.Raycaster | null>(null);

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
    light2.castShadow = true;
    light2.position.set(1, 4, 0);
    light2.shadow.mapSize.width = light2.shadow.mapSize.height = 1024 * 10;
    light2.shadow.radius = 4;
    light2.shadow.bias = 0.0001;
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

        // scene.current?.add(new THREE.BoxHelper(obj3d))
        
        // 자동차는 그림자  던지고 받고
        obj3d.traverse(child => {
          child.castShadow = true;
          child.receiveShadow = true;
        })
      })
    })

    const boxGeometry = new THREE.CylinderGeometry(1.2, 1.2, 0.1, 64);
    const boxMaterial = new THREE.MeshStandardMaterial({
      color: 0x454545,
      metalness: 0.5,
      roughness: 0.5
    });
    const box = new THREE.Mesh(boxGeometry, boxMaterial);

    // mesh는 그림자 받기만
    box.receiveShadow = true;
    box.name = "box";

    box.position.set(0, -0.05, -0.3)
    scene.current?.add(box)
  };

  const SetupPicking = () => {
    const raycaster = new THREE.Raycaster();
    divContainer.current?.addEventListener("dblclick", OnDblClick);
    raycasterRef.current = raycaster;
  }

  const OnDblClick = (event:any) => {
    if (event.isPrimary === false) return;

    // 현재 마우스의 위치 찾기
    const mouse = new THREE.Vector2
    mouse.set((event.clientX / window.innerWidth) * 2 - 1, -(event.clientY / window.innerHeight) * 2 + 1);

    raycasterRef.current?.setFromCamera(mouse, camera.current!)
    
    // 객체 이름이 car인 객체만 고르기
    const cars:THREE.Object3D[] = [];
    scene.current?.traverse( (obj3d) => {
      if (obj3d.name === "car") {
        cars.push(obj3d);
      }
    })
    
    // 더블 클릭된 곳과 해당 객체의 충돌점을 찾아서 객체를 정확히 추적
    for(let i=0; i<cars.length; i++) {
      const car = cars[i];

      const targets = raycasterRef.current?.intersectObject(car);
      if(targets!.length > 0) {
        // 더블클릭된 차 확대 
        ZoomFit(car, 70)
        return;
      }
    }

    const box = scene.current?.getObjectByName("box");
    // 무대 확대 코드
    ZoomFit(box!, 45)

  }


  /** 확대 실행 학수 */
  const ZoomFit = (object3d:THREE.Object3D, viewAngle:number) => {
    // 객체를 감싸고 있는 box
    const box = new THREE.Box3().setFromObject(object3d);
    // 객체의 정육각형 box의 대각선 길이
    const sizeBox = box.getSize(new THREE.Vector3()).length();
    // box의 중앙점
    const centerBox = box.getCenter(new THREE.Vector3());

    // 처음에 설정된 벡터
    const direction = new THREE.Vector3(0, 1, 0);
    // 처음에 설정된 벡터 (0, 1, 0)을 (1, 0 ,0)방향으로 viewAngle만큼 회전한 객체
    direction.applyAxisAngle(new THREE.Vector3(1, 0, 0),
      THREE.MathUtils.degToRad(viewAngle));

    // sizebox의 절반
    const halfSizeModel = sizeBox * 0.5;
    // 카메라 fov의 절반
    const halfFov = THREE.MathUtils.degToRad(camera.current!.fov * 0.5);
    // 모델을 확대했을 때, 거리값
    const distance = halfSizeModel / Math.tan(halfFov);
    // 카메라의 새로운 위치 
    // 단위 벡터 * distance 로 방향벡터를 얻고
    // 위치 벡터인 centerBox를 추가하여 
    // 정확한 위치를 얻어냄 
    const newPosition = new THREE.Vector3().copy(
      direction.multiplyScalar(distance).add(centerBox)
    );

    // camera.current?.position.copy(newPosition);
    // 동적으로 변경
    gsap.to(camera.current!.position, {
      duration: 0.5,
      x: newPosition.x, y: newPosition.y, z: newPosition.z
    })

    // controls.current?.target.copy(centerBox);
    gsap.to(controls.current!.target, {
      duration: 0.5,
      x: centerBox.x,
      y: centerBox.y,
      z: centerBox.z,
      // 매 프레임마다 카메라의 위치 추적
      onUpdate: () => {
        camera.current!.lookAt(
          controls.current!.target.x,
          controls.current!.target.y,
          controls.current!.target.z,
        )
      }
    })
    
  }
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

    controls.current?.update()

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

      SetupPicking();
      // divContainer.current.addEventListener("dblclick", OnDblClick, false);

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