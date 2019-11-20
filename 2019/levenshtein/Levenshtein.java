/**
 * Levenshtein problem 2019
 * Created by: Colter Boudinot
 * Points awarded: yes
 * Status: complete
 */

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Levenshtein
{

	public static void main(String[] args)
	{
		// TODO Auto-generated method stub
		Scanner input = new Scanner(System.in);

		String line1 = input.next();
		String line2 = input.next();

		ArrayList<String> wordList = new ArrayList<String>();

		// remove letter

		for (int i = 0; i < line2.length(); i++)
		{
			String wordToAdd = line2.substring(0, i) + line2.substring(i + 1);
			if(wordList.contains(wordToAdd) == false)
				wordList.add(wordToAdd);
		}

		// add letter
		for (int j = 0; j < line1.length(); j++)
		{
			for (int i = 0; i < line2.length() + 1; i++)
			{
				String wordToAdd = line2.substring(0, i) + line1.substring(j, j + 1) + line2.substring(i);
				if(wordList.contains(wordToAdd) == false)
					wordList.add(wordToAdd);
			}

		}

		// replace letter

		for (int j = 0; j < line1.length(); j++)
		{
			for (int i = 0; i < line2.length(); i++)
			{
				String wordToAdd = line2.substring(0, i) + line1.substring(j, j + 1) + line2.substring(i + 1);
				if(wordList.contains(wordToAdd) == false)
					wordList.add(wordToAdd);
			}

		}
		
//		for (int i = 0; i < wordList.size(); i++)
//		{
//			if(wordList.get(i).equals(line2))
//			{
//				wordList.remove(i);
//			}
//		}

		wordList.remove(line2);

		wordList.sort(null);
		for (int i = 0; i < wordList.size(); i++)
		{
			System.out.println(wordList.get(i));
		}

	}

}
