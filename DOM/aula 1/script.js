var p = document.getElementsByTagName('p')

//alert(p.length)

//alert(p[0].innerHTML)

//p[0].innerHTML = 'Manipulado via JS'

/*for (i = 0; i < 5; i++) {
    p[i].innerHTML = ('Manipulado via JS '+ i)
}*/

for(i = 0; i < 10; i++){
    p[0].innerHTML = p[0].innerHTML + i
}