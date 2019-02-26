# AMENDMENT_EMPLOYMENT

## Procedure

First I found that all the employment files had no "AMEND' word in it. So i used this criteria to separate all the amendmend files and the employment files. 

Two of the files were giving errors, thats why I used the try except block of code.

Next I used regex to replace all the extra spaces and extra new lines.

Then I used sentence tokenizer to tokenize a file. Then word tokenized all the files. I removed all the stop words and the non alpha numeric characters. Then I removed all the noun words using POS tag(search for NN as POS).

I created an outcome list which shall have 0 and 1 as values. 0 representing an amended file, and 1 representing an employment file.

I made a list "document". Each index of this document shall have two items. Tokenized amended or employment words followed by a 0 or 1.
Then I shuffled the document in random order.

For building my classifier:

I took all the words present in the document list (around 9lakhs of them). Used the frequency distribution to take the top 10000 words. These 10000 words act as my look up table.

Next I send the words that is d[0] from each document and find whether or not the words are present in this look up table. The function returns feature set with True or False values, corresponding to whether or not the words are present in the look up table.

I created tuples with this feature set and outcome( that is 0 and 1). I put this in the naive bayes classifier to predict my accuracy score. A Tfidf Vectorizer can also be used. But since it is a classifier based problem, so I thought a Naive bayes will be good enough.

I printed the accuracy score along with the most informative features.

## Extract

I cound find salary and dates. I couldnt find an effective way to extract the names of employer and employee using NER.

I extracted salary and dates using regex.

## Improvements

Improvements can be made by chunking Named Entities and Lametization.
