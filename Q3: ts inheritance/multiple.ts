interface Person{
    name: string
}

interface PersonDetails{
    age: number
    gender: string
}

interface Employee extends Person,PersonDetails{
    empCode: number
}

let empObject = <Employee>{};
empObject.name = "Rhea"
empObject.age = 19
empObject.gender = "Female"
empObject.empCode = 42354

console.log("Name: "+empObject.name);
console.log("Employee Code: "+empObject.empCode);