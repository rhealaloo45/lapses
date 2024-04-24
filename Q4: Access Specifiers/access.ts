class Student {
	public  studcode: number;
	protected studname: string
	constructor(code: number, name: string){
		this.studcode = code;
		this.studname = name;
	}
}
class Person extends Student {
	private department: string;
	constructor(code: number, name: string, department: string){
		super(code, name)
		this.department = department
	}
	public getinfo() {
		return (`${this.studcode}, ${this.studname}, ${this.department}`)
	}
}
let joeRoot : Person = new Person(309, "Yash the great", "Info Tech");
console.log(joeRoot.getinfo());
