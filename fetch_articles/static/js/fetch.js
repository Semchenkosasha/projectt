let root = document.getElementById('root')
root.innerHTML = '<div class="root_article"></div>'
let article = document.querySelector(".root_article")

function fn(){
    fetch('http://127.0.0.1:8000/api/get_articles_list/')
        .then(resp => resp.json())
        .then(data => {
            console.log(data)
            data.map(item => {
                article.innerHTML += `<div>
                    <p>${item.title}</p>
                    <img src="${item.preview_img}">
                </div>`
            })
        })
}

fn()