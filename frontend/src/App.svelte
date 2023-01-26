<script>

let message;

fetch("http://192.168.0.43:7443/hello").then((response) => {
    response.json().then((json) => {
        message = json.message;
    });
});

</script>


<h1>안녕하세요 파이보</h1>