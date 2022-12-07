import "web/main/components/Main.css"

const Main = ()=> {
    return(<>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossOrigin="anonymous"/>
    
    <table className="container-fluid">
        <thead></thead>
        <tbody>
            <tr id='service' style={{height: "1080px"}}>service</tr>
            <tr className="white" id="howto" style={{height: "1080px"}}>howto</tr>
            <tr id="notice" style={{height: "1080px"}}>mapping</tr>
        </tbody>
    </table></>)
}

export default Main