// import * as THREE from "three";

// class App {
//   constructor() {
//     const divContainer = document.querySelector("container")
//     this._divContainer = divContainer;

//     const renderer = new THREE.WebGLRenderer({ antialias: true});
//     renderer.setPixelRatio(window.devicePixelRatio);
//     divContainer?.appendChild(renderer.domElement);
//     this._renderer = renderer;

//     const scene = new THREE.Scene();
//     this._scene =scene;

//     this._setupCamera();
//     this._setupLight();
//     this._setupModel();

//     window.onresize = this.resize.bind(this);
//     this.resize();

//     requestAnimationFrame(this.render.bind(this));

//   }

//   _setupCamera() {
//     const width = this._divContainer.clientWidth
//     const height = this._divContainer.clientHeight
//     const camera = new THREE.PerspectiveCamera(
//       75,
//       width / height,
//       0.1,
//       100
//     );
//     camera.position.z = 2;
//     this._camera = camera;
//   }

//   _setupLight() {
//     const color = 0xffffff;
//     const intensity = 1;
//     const light = new THREE.DirectionalLight(color, intensity)
//     light.position.set(-1, 2, 4)
//     this._scene.add(light);
//   }

//   _setupModel () {
//     const geometry = new THREE.BoxGeometry(1, 1, 1);
//     const meterial = new THREE.MeshPhongMaterial({color: 0x44a88});

//     const cube = new THREE.Mesh(geometry, meterial);

//     this._scene.add(cube);
//     this._cube = cube;
//   }

//   resize() {
//     const width = this._divContainer.clientWidth;
//     const height = this._divContainer.clientHeight;

//     this_camer.aspect = width / height;
//     this._camera.updateProjectionMatrix();

//     this._renderer.setSize(width, height);
//   }

//   render(time) {
//     this._renderer.render(this._scene, this._camera);
//     this.update(time);
//     requestAnimationFrame(this.render.bind(this));
//   }

//   update(time) {
//     time *= 0.001;
//     this._cube.rotation.x = time;
//     this._cube.rotation.y = time;
//   }
// }

// window.onload = function() {
//   new App();
// }

import * as THREE from "three";

import { useEffect, useRef } from "react";

const App = () => {
  const divContainer = useRef<HTMLDivElement>(null);
  const renderer = useRef<THREE.WebGLRenderer | null>(null);
  const scene = useRef<THREE.Scene | null>(null);
  const camera = useRef<THREE.PerspectiveCamera | null>(null);
  const cube = useRef<THREE.Mesh | null>(null);

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
    const geometry = new THREE.BoxGeometry(1, 1, 1);
    const material = new THREE.MeshPhongMaterial({ color: 0x44a88 });

    const mesh = new THREE.Mesh(geometry, material);

    scene.current?.add(mesh);
    cube.current = mesh;
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
    time *= 0.01;
    cube.current!.rotation.x = time;
    cube.current!.rotation.y = time;
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

export default App;