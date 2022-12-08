import { Link } from "react-router-dom"


const MngMenu=()=>{
    return(<>
    <div>
        <Link to ="/mn"><button>관리자 메인</button></Link><br/>
        <Link to ="*/mnguserinfo"><button>회원 조회</button></Link><br/>
        <Link to ="*/mngdamage"><button>파손기록</button></Link><br/>
        <Link to ="*/mngclaim"><button>상담 내역</button></Link><br/>
        <Link to ="*/mngbox"><button>보관함 관리</button></Link><br/>
        <Link to ="*/mngdemand"><button>수요 예측</button></Link><br/>
        <Link to ="*/mngnotice"><button>공지사항 관리</button></Link><br/>

        
    </div>
    </>)
}
export default MngMenu