import * as THREE from "three";

import { useEffect, useRef } from "react";

import { OrbitControls } from "three/examples/jsm/controls/OrbitControls";
import bg from "../assets/img/image.jpg"
import cube1 from "../assets/img/posx.jpg"
import cube2 from "../assets/img/negx.jpg"
import cube3 from "../assets/img/posy.jpg"
import cube4 from "../assets/img/negy.jpg"
import cube5 from "../assets/img/posz.jpg"
import cube6 from "../assets/img/negz.jpg"
import square from "../assets/img/cannon.jpeg"

const Background = () => {
  const divContainer = useRef<HTMLDivElement>(null);
  const renderer = useRef<THREE.WebGLRenderer | null>(null);
  const scene = useRef<THREE.Scene | null>(null);
  const camera = useRef<THREE.PerspectiveCamera | null>(null);
  const sphere = useRef<THREE.Mesh | null>(null);
  const controls = useRef<OrbitControls |null>(null);

  /** 카메라 커스텀 함수 */
  const SetupCamera = () => {
    const width = divContainer.current?.clientWidth || 0;
    const height = divContainer.current?.clientHeight || 0;
    const cam = new THREE.PerspectiveCamera(
      75, 
      width / height, 
      0.1, 
      1000
    );
    cam.position.z = 80;
    camera.current = cam;
  };

  /** 조명 커스텀 함수 */
  const SetupLight = () => {
    const color = 0xffffff;
    const intensity = 1.5;
    const light = new THREE.DirectionalLight(color, intensity);
    light.position.set(-1, 2, 4);
    scene.current?.add(light);
  };

  /** 모델 커스텀 함수 */
  const SetupModel = () => {
    if (!renderer.current || !scene.current) return

    const pmremG = new THREE.PMREMGenerator(renderer.current);
    // SetupModel이 없는 상태에서 background를 받으려니 문제 생김!
    // => Backround를 호출할 때, 모델을 호출해주자

    // 객체에 배경이 비춰지게 함
    const background = scene.current.background;
    if (background instanceof THREE.CubeTexture) {
      const renderTarget = pmremG.fromEquirectangular(background);
      // const renderTarget = pmremG.fromCubemap(background);

      const geometry = new THREE.SphereGeometry();

      //재질
      const material1 = new THREE.MeshStandardMaterial({
        color: "#2ecc71",
        roughness: 0,
        metalness: 1,
        envMap: renderTarget.texture
      })

      const material2 = new THREE.MeshStandardMaterial({
        color: "#e74c3c",
        roughness: 0,
        metalness: 1,
        envMap: renderTarget.texture
      })
    
      const rangeMin = -20.0, rangeMax = 20.0;
      const gap = 10.0;
      let flag = true;

      for (let x = rangeMin; x <= rangeMax; x += gap) {
        for (let y = rangeMin; y <= rangeMax; y += gap) {
          for (let z = rangeMin*10; z <= rangeMax; z += gap) {
            flag = !flag;

            const mesh = new THREE.Mesh(geometry, flag ? material1 : material2);

            mesh.position.set(x, y, z);

            scene.current?.add(mesh);
          }
        }
      }
    }
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

  /** 배경함수 */
  const Background = () => {

    // //1. 안개 : 안개의 색상과 배경의 색상을 동일하게 줘야 효과 있음`
    // scene.current.background = new THREE.Color("#9b59b6");
    // scene.current.fog = new THREE.Fog("#9b59b6", 0, 150); // 안개의 색상, 안개 시작거리, 가시거리
    // scene.current.fog = new THREE.FogExp2("#9b59b6", 0.02);  // 카메라부터 멀어질 수록 안개 생김, 두번째 인자는 안개의 강도
  
    // //2. 이미지를 배경으로 (방법 여러개지만, 여기서는 Texture 이용)
    // const loader = new THREE.TextureLoader();

    // loader.load(bg, texture => {
    //     scene.current!.background = texture;
        
    //     // SetupModel이 없는 상태에서 background를 받으려니 문제 생김!
    //     // => Backround를 호출할 때, 모델을 호출해주자
    //     SetupModel();
    // })

    // //3. 큐브맨을 사용하여 동적인 배경 가능
    // const loader = new THREE.CubeTextureLoader();
    // loader.load([
    //   cube1,
    //   cube2,
    //   cube3,
    //   cube4,
    //   cube5,
    //   cube6
    // ], cubeTexture  => {
    //   scene.current!.background = cubeTexture;
    //   SetupModel();      
    // })

    //4. 정방형 맵을 사용해서 배경
    const loader = new THREE.TextureLoader();

    loader.load(square, texture => {
      const renderTarget = new THREE.WebGLCubeRenderTarget(texture.image.height);
      renderTarget.fromEquirectangularTexture(renderer.current!, texture);
      scene.current!.background = renderTarget.texture;
      SetupModel();

    })
  } 

  const render = (time: number) => {
    renderer.current?.render(scene.current!, camera.current!);
    update(time);
    requestAnimationFrame(render);
  };

  const update = (time: number) => {
    time *= 0.01;
    // sphere.current!.rotation.x = time;
    // sphere.current!.rotation.y = time;
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
      // SetupModel();
      SetupControls();
      Background();

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

export default Background;