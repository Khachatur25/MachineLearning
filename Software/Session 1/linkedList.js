class Node{
	constructor(data){
		this.data = data;
		this.next = null;
	}
}

class LinkedList{
	constructor(){
		this.head = null;
	}

	add_from_end(data){
		let  new_node = new Node(data);
		if (!this.head){
			this.head = new_node
		}
		else{
			let current = this.head
			while (current.next){
				current = current.next
			}
			current.next =  new_node
		}
	}

	print_node(){
		if(!this.head){
			console.log('[]')
		}
		else{
			console.log('[')
			let current = this.head;
			while(current){
				console.log(current.data,',')
				current = current.next;
			}
			console.log(']')
		}
	}
}

let ll = new LinkedList();
ll.add_from_end(10);
ll.add_from_end(4);
ll.add_from_end(16);
ll.print_node();
