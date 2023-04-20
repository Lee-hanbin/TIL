import * as THREE from "three";

import React, { useEffect, useRef, useState } from 'react';

function basic() {
  // const divContainer = document.querySelector("div")
  const DivRef = useRef<HTMLDivElement | null>(null);

  // 카메라 초기 세팅  
  const defaultCamera = new THREE.PerspectiveCamera(
    75,
    window.innerWidth / window.innerHeight,
    0.1,
    100
  );

  const cameraRef = useRef<THREE.PerspectiveCamera>(defaultCamera);


  /** 카메라 커스텀 함수 */
  const setupCamera = () => {
    cameraRef.current.position.z = 2;
  }

  /** 조명 커스텀 함수 */
  const setupLight = () => {

  }

  const setupModel = () => {

  }

  useEffect(() => {
    if (!DivRef.current) return;

    const camera = cameraRef.current;
    camera.position.set(0, 50, 170);

    const renderer = new THREE.WebGLRenderer({ 
      canvas: DivRef.current!, 
      antialias : true // 계단현상 없음
    });

    renderer.setSize(window.innerWidth, window.innerHeight);
    DivRef.current.appendChild(renderer.domElement);
    
    const scene = new THREE.Scene();
    
    setupCamera

    const animate = () =>  {
      requestAnimationFrame( animate );

      // model.rotation.x += 0.01;
      // model.rotation.y += 0.01;

      renderer.render( scene, camera );
    }

    animate();
      
    // 조명 초기 세팅
    const color = 0xffffff;
    const intensity = 1;
    const light = new THREE.DirectionalLight(color, intensity);
    light.position.set(-1, 2, 4);

    window.addEventListener("resize", () => {
      renderer.setSize(window.innerWidth, window.innerHeight);
      camera.aspect = window.innerWidth / window.innerHeight;
      camera.updateProjectionMatrix();
    });

  })

  return (
    <div ref={DivRef}>basic</div>
  )
}

export default basic;