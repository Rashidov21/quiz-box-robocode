let answer_list = document.querySelectorAll('.answer_list div')
let answer_list_i = document.querySelectorAll('.answer_list button i')
for (let i = 0; i < answer_list.length; i++) {
    answer_list[i].addEventListener('click', () => {
        for (let k = 0; k < answer_list.length; k++) {
            answer_list[k].classList.remove('active')
            answer_list_i[k].classList.remove('fa-solid' , 'fa-check')
        }
        answer_list[i].classList.add('active')
        answer_list_i[i].classList.add('fa-solid', 'fa-check')
    })
}