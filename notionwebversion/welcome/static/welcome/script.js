function MyFunction(){
    let element = document.body
    element.classList.toggle("body-dark");
    
    let header = document.getElementsByClassName('header')[0]
    header.classList.toggle("header-dark");

    let alist = document.getElementsByClassName('nav-a')
    
    for (let i = 0; i < alist.length; i++) {
        alist[i].classList.toggle("nav-a-dark")
      }
    
    let buttontheme = document.getElementsByClassName('button')[0]
    buttontheme.classList.toggle("button-dark");


    let waves_light = document.getElementsByClassName('waves-light')[0]
    waves_light.classList.toggle('unvisible');
    
    let waves_dark = document.getElementsByClassName('waves-dark')[0]
    waves_dark.classList.toggle('unvisible');

    let logo_dark = document.getElementsByClassName('logo')[0]
    logo_dark.classList.toggle('unvisible');

    let logo_light = document.getElementsByClassName('logo-dark')[0]
    logo_light.classList.toggle('unvisible');


}   

function Visible_div(){
    let more = document.getElementsByClassName('div_more')[0]
    more.classList.toggle('visible')
}