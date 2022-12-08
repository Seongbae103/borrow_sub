const MngNotice = () => {
    return(<>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossOrigin="anonymous"/>
    <h3>공지 사항</h3>
    <input type="string" class="form-control" id="inputGroupFile01"/>
    <div class="input-group mb-3">
        <label class="input-group-text" for="inputGroupFile01">Upload</label>
        <input type="file" class="form-control" id="inputGroupFile01"/>
    </div>
    <button type="button" class="btn btn-success">공지사항 업로드</button>
    </>)
}
export default MngNotice