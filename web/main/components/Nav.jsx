import { Link } from "react-router-dom"


const Nav=()=>{
    return(<>
    <nav className="navbar navbar-expand-lg gnav">
        <div className="container-fluid">
            <a className="navbar-brand" href ="/main">Borrow-San</a>
                
            <div className="collapse navbar-collapse" id="navbarSupportedContent">
                <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                <li className="nav-item">
                    <a className="nav-link active" aria-current="page" href="#service" >서비스 소개</a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="#howto">이용방법</a>
                </li>
                <li className="nav-item">
                    <Link to ="/notice" className="nav-link">공지사항</Link>
                </li>
                <li className="nav-item">
                    <Link to ="/mn/*" className="nav-link">관리자</Link>
                </li>
            </ul>
            </div>
        </div>
    </nav>
    </>)
}
export default Nav