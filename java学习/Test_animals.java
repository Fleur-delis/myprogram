class Test_animals {
	public static void main(String[] args) {
		Cat cat = new Cat();
		cat.setName("miao");
		cat.setAge(10);
		cat.eat();
		cat.catchfish();
		System.out.println(cat.getName() + "..." + cat.getAge());
		System.out.println("-------------------------------");
		Dog dog = new Dog("wang",12);
		dog.eat();
		dog.lookhome();
		System.out.println(dog.getName() + "..." + dog.getAge());
	}
}


class Animals {
	private String name;
	private int age;

	public Animals(){};

	public Animals(String name,int age){
		this.age = age;
		this.name = name;
	}
	public void eat(){
		System.out.println("吃饭");
	}

	public void setName(String name){
		this.name = name;
	}

	public String getName(){
		return name;
	}

	public void setAge(int age){
		this.age = age;
	}

	public int getAge(){
		return age;
	}
}

class Dog extends Animals{
	public Dog(){};

	public Dog(String name,int age){
		super(name,age);
	}

	public void lookhome(){
		System.out.println(super.getName() + "会看家");
	}
}

class Cat extends Animals{
	public Cat(){};

	public Cat(String name,int age){
		super(name,age);
	}
	public void catchfish(){
		System.out.println(super.getName() + "会抓鱼");
	}
}
