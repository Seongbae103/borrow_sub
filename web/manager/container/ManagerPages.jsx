import { Route, Routes, Link } from "react-router-dom"
import {MngNotice, MngClaim, MngBox, MngDamage, MngDemand} from "web/manager"

const ManagerPages = ()=>{
    return(<>
    <div>관리자명</div>
    <div>
        <button><Link to ="#">공지사항 작성</Link></button><br/>
        <button><Link to ="/mn/userinfo">유저 정보</Link></button><br/>
        <button><Link to ="/mn/claim">상담 내역</Link></button><br/>
        <button><Link to ="/mn/box">보관함 조회</Link></button><br/>
        <button><Link to ="/mn/damage">파손기록</Link></button><br/>
        <button><Link to ="/mn/demand">수요예측</Link></button><br/>
    </div>
    <div>
        <Routes>
            <Route path="/mn/claim" element={<MngClaim/>}></Route>
            <Route path="/mn/box" element={<MngBox/>}></Route>
            <Route path="/mn/damage" element={<MngDamage/>}></Route>
            <Route path="/mn/demand" element={<MngDemand/>}></Route>
        </Routes>
    </div>
    </>)
}

export default ManagerPages