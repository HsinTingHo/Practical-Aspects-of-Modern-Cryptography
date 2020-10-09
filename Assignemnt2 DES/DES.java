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
*/

/* key: 0123456789ABCDEF
 * plain text: 789AB123456789AA
 * cipher text: e7ab74f51fb2e8a4
 */

import java.util.Arrays;

public class DES {
	public DES(String msg, String key) {
		System.out.println(msg);
		Public_Tables tables = new Public_Tables();
		
		
		
		//perform PC_1 to shrink key from 64 bits to 56 bits
		//perform initial permutation on msg and split msg into left half and right half
		//perform transformation on key and encrypt for 16 times
			//transformation 56 bits key to 48 bits
			//perform f on 48 bits key and right half of msg
			//new_right = XOR the result with left half of msg
			//new_left = right half
		//final permutation
	}
//    private static final byte[] IP = { 
//            58, 50, 42, 34, 26, 18, 10, 2,
//            60, 52, 44, 36, 28, 20, 12, 4,
//            62, 54, 46, 38, 30, 22, 14, 6,
//            64, 56, 48, 40, 32, 24, 16, 8,
//            57, 49, 41, 33, 25, 17, 9,  1,
//            59, 51, 43, 35, 27, 19, 11, 3,
//            61, 53, 45, 37, 29, 21, 13, 5,
//            63, 55, 47, 39, 31, 23, 15, 7
//        };
	
}
