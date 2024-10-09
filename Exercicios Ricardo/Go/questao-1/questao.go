package main

import "fmt"

type Carro struct {
    marca  string
    modelo string
    ano    int
}
func main() {
    carro1 := Carro{"Ferrari", "Italia", 1998}
    carro2 := Carro{"Chevrolet", "Celta", 2021}
    carro3 := Carro{"Chevrolet", "Onix", 2019}
   
    fmt.Println(carro1)
    fmt.Println(carro2)
    fmt.Println(carro3)
}