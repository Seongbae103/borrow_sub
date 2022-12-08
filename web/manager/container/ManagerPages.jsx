import { Route, Routes } from "react-router-dom"
import {MngMenu, MngClaim, MngBox, MngDamage, MngDemand, MngNotice} from "web/manager"
import "web/manager/style/Manager.css"
import MngUserInfo from "../components/MngUserInfo"

const ManagerPages = ()=>{
    return(<>
    <table>
    <thead>관리자명</thead>
    <tbody><MngMenu/></tbody>
    </table>
    <body className="bgc">
        <Routes>
            <Route path="/mn" element={<ManagerPages/>}></Route>
            <Route path="*/mngclaim" element={<MngClaim/>}></Route>
            <Route path="*/mngbox" element={<MngBox/>}></Route>
            <Route path="*/mngdamage" element={<MngDamage/>}></Route>
            <Route path="*/mnguserinfo" element={<MngUserInfo/>}></Route>
            <Route path="*/mngdemand" element={<MngDemand/>}></Route>
            <Route path="*/mngnotice" element={<MngNotice/>}></Route>
        </Routes>
    </body>
    </>)
}

export default ManagerPages