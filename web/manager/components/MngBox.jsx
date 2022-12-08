import "web/manager/style/Manager.css"
const MngBox =()=>{
    return(<>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossOrigin="anonymous"/>
    <h3>보관함 조회</h3>
    <table class="table">
        <thead>
            <td>
                <th scope="col">보관함 ID</th>
                <th scope="col">위치</th>
                <th scope="col">잔여수량</th>
                <th scope="col">재고 부족 비율</th>
            </td>
        </thead>
        <tbody className="bgc">
            <tr>
                <td>
                    <th scope="row">1</th>
                    <th>00시 ??구</th>
                    <th>6</th>
                    <th>?? %</th>
                </td>
            </tr>
            <tr>
                <td>
                    <th scope="row">2</th>
                    <th>00시 ??구</th>
                    <th>6</th>
                    <th>?? %</th>
                </td>
            </tr>
            <tr>
                <td>
                    <th scope="row">3</th>
                    <th>00시 ??구</th>
                    <th>6</th>
                    <th>?? %</th>
                </td>
            </tr>
        </tbody>
    </table>
    </>)
}

export default MngBox