import Background from "../components/10_Background";
import Basic from "../components/01_Basic";
import Camera from "../components/07_Camera";
import CustomGeometry from "../components/05_CustomGeometry";
import FontGeometry from "../components/12_FontGeometry";
import Geometry from "../components/02_Geometry";
import Light from "../components/06_Light";
import Material from "../components/04_Material";
import React from 'react';
import SceneGraph from "../components/03_SceneGraph";
import Shadow from "../components/08_Shadow";
import Zoom from "../components/09_Zoom";
import ZoomInOut from "../components/11_ZoomInOut";
import Ranking from "../components/12_Ranking";

function IntroPage() {

  return (
    <body>
      {/* <Basic /> */}
      {/* <Geometry /> */}
      {/* <SceneGraph /> */}
      {/* < Material /> */}
      {/* <CustomGeometry /> */}
      {/* <Light /> */}
      {/* <Camera /> */}
      {/* <Shadow / > */}
      {/* <Zoom /> */}
      {/* <Background /> */}
      {/* <ZoomInOut /> */}
      <Ranking />
      <FontGeometry />
    </body>
  )
}

export default IntroPage;