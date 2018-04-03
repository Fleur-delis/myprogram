/*class Extends {
	public static void main(String[] args) {
		Cat cat = new Cat();
		cat.setName("喵喵");
		cat.age = 10;
		cat.feed();
		System.out.println("Name = " + cat.getName() + "Age = " + cat.age);
	}
}


class Animals{
	private String name;
	int age;

	public void feed(){
		System.out.println("吃");
	}

	public void setName(String name ){
		this.name = name;
	}

	public String getName(){
		return name;
	}
}
class Cat extends Animals {};*/
class Fu {
	static {
		System.out.println("静态代码块Fu");
	}

	{
		System.out.println("构造代码块Fu");
	}

	public Fu() {
		System.out.println("构造方法Fu");
	}
}

class Zi extends Fu {
	static {
		System.out.println("静态代码块Zi");
	}

	{
		System.out.println("构造代码块Zi");
	}

	public Zi() {
		System.out.println("构造方法Zi");
	}
}
class Extends {
	public static void main(String[] args) {
		Zi z = new Zi();
	}
}