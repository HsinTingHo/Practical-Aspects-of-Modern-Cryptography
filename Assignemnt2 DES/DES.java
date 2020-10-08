/*Algorithm
constructor(msg, 64 bits key)
PC_1
PC_2
transformation
rotate_right
rotate_left
initial_permutation
final_permutaiton
feistel_function
s_1_to_8
permutation
expansion_32_48
permutation table reference: https://cafbit.com/resource/DES.java
*/
public class DES {
	public DES(String msg, String key) {
		System.out.println(msg);
		//perform PC_1 to shrink key from 64 bits to 56 bits
		//perform initial permutation on msg and split msg into left half and right half
		//perform transformation on key and encrypt for 16 times
			//transformation 56 bits key to 48 bits
			//perform f on 48 bits key and right half of msg
			//new_right = XOR the result with left half of msg
			//new_left = right half
		//final permutation
	}
}
