import java.util.ArrayList;
//hashtable implemetation from 
//https://www.geeksforgeeks.org/implementing-our-own-hash-table-with-separate-chaining-in-java/

//use LinkedList to help create hashtable
class Node<K,V>{
	K  key;
	V value;

	//Next node
	Node<K,V> next;

	//Constructor
	public Node (K key, V value){
		this.key = key;
		this.value = value;
	}

}

//the hashtable
class Map<K,V>{
	//arrayList to store linked lists
	private ArrayList<Node<K,V>> linkedArray;

	//size of linkedLists
	private int arraySize;

	//size of linkedArray
	private int size;

	//Constructor
	public Map(){
		linkedArray = new ArrayList();
		arraySize = 10;
		size = 0;

		//initialize the arraylist
		for(int i = 0; i < arraySize;i++){
			linkedArray.add(null);
		}
	}

		public int size() { return size; }
		public boolean isEmpty() { return size() == 0; }


	//finds the index for the key
	private int getArrayIndex (K key){
		int hashCode = key.hashCode();
		int index = hashCode % arraySize;
		return index;
	}

	//remove a key
	public V remove(K key){
		//find the index
		int arrayIndex = getArrayIndex(key);

		//get head of list
		Node<K,V> head = linkedArray.get(arrayIndex);
		//Node already visited
		Node<K,V> prev = null;

		while(head != null){
			//if Key found
			if(head.key.equals(key)){
				break;
			}

			//Else check the next node
			prev = head;
			head = head.next;
		}

		//if key was not found
		if(head == null){
			return null;
		}

		//reduce size
		size --;

		//remove the key
		if(prev != null){
			prev.next = head.next;
		}
		else{
			linkedArray.set(arrayIndex,head.next);
		}
		return head.value;
	}

	//return value for a key
	public V get(K key){
		//get the head of the key
		int arrayIndex = getArrayIndex(key);
		Node<K,V> head = linkedArray.get(arrayIndex);

		//search for the key in list
		while(head != null){
			if(head.key.equals(key)){
				return head.value;
			}
			head = head.next;
		}
		return null;
	}

	//Adds a key value pair to hash
	public void add(K key, V value){
		//get the head of the key
		int arrayIndex = getArrayIndex(key);
		Node<K,V> head = linkedArray.get(arrayIndex);

		//check if key is alreadyt here
		while(head != null){
			if(head.key.equals(key)){
				head.value = value;
				return;
			}
		}

		//insert the key
		size++;
		head = linkedArray.get(arrayIndex);
		Node<K,V> newNode = new Node<K,V>(key,value);
		newNode.next = head;
		linkedArray.set(arrayIndex, newNode);

		//if load factor goes beyond threshold then double the hash table size
		if((1.0*size)/arraySize >= 0.7){
			ArrayList<Node<K,V>> temp = linkedArray;
			linkedArray = new ArrayList<>();
			arraySize = 2*arraySize;
			size = 0;
			for(int i = 0; i < arraySize;i++){
				linkedArray.add(null);
			}
			for(Node<K,V> headNode : temp){
				while (headNode != null){
					add(headNode.key, headNode.value);
					headNode = headNode.next;
				}
			}
		}
	}
	public static void main(String[] args){
	        Map<String, Integer>map = new Map<>();
	        map.add("this",1 );
	        map.add("coder",2 );
	        map.add("this",4 );
	        map.add("hi",5 );
	        System.out.println(map.size());
	        System.out.println(map.remove("this"));
	        System.out.println(map.remove("this"));
	        System.out.println(map.size());
	        System.out.println(map.isEmpty());
    	}


}