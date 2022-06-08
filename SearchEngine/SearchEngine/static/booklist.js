const searchField = document.getElementById('searchField')

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');

searchField.addEventListener('keyup',(event)=>{
    const searchValue = event.target.value;
    if (searchValue.trim().length>0){
        console.log('search-value', searchValue)
        fetch('search-book/',{
            headers:{'X-CSRFToken': csrftoken},
            body: JSON.stringify({searchText:searchValue}),
            method:"POST",
        })
        .then((res)=>res.json())
        .then((data)=>{
            console.log("data", data);

        })
    }
})