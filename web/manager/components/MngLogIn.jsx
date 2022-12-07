import { useState } from "react"
import { Link } from "react-router-dom"

const MngLogin = () => {
    const [inputs, setInputs] = useState({})
    const {email, password} = inputs;

    const onChange = e => {
        e.preventDefault()
        const {value, name} = e.target 
        setInputs({...inputs, [name]: value})
    }

    const onClick = e => {
        e.preventDefault()
        const request = {email, password}
        alert(`사용자 이름: ${JSON.stringify(request)}`)

    }

    return (
    <>
        EMAIL: <input type="text" name="email" onChange={onChange} /><br/>
        PASSWORD: <input type="text" name="password" onChange={onChange} /><br/>
        <button onClick={onClick}> 로그인 </button>
    </>
)}
export default MngLogin