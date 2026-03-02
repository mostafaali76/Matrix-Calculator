#Task:Core Numpy OPerations: students grades
#Step1:calling Numpy Library and giving it a nickname (np) for convenience
import numpy as np
#Step2:converting the data into numpy arrays
grades=np.array([[85, 78, 92, 88],   #1st student
                 [70, 76, 80, 65],   #2nd student
                 [90, 88, 94, 91],   #3rd student
                 [60, 65, 58, 62],   #4th student
                 [100, 95, 98, 97]] )#5th student
#Step3: Shape of the array using SHAPE property
print("Shape: ",grades.shape)
#Step4: the mean grade of each student
#Note: since that the grades of each student are nothing but COLUMNs, so we'll set our axis=1
mean_student_grade=np.mean(grades,axis=1)
print("\nThe avarage grade per student: ", mean_student_grade )
#A better form for step4 by reshaping the mean array into a column one, knowing that each column represents each student
print('Or in a better form: \n', mean_student_grade.reshape(-1, 1))
#Step5: the mean per subject
#note: since that each subject's grade for each student is in a row, so we'll go accross rows by setting axis=0
mean_subject_grade=np.mean(grades, axis=0)
print('\nMean grade of each subject: ',mean_subject_grade)
#Step 6: Filtering out the avarage of students'grades >85
print('\nAverage student grade greater than 85: ',mean_student_grade[mean_student_grade>85])
#Step 7: Adding a bonus of 5 marks to all grades
#since that this operation is called scalar addition of matrices
#and since mathematically It's illegal to add an object to a matrix unless they're both of the same dimensions
#therefore, the most proper method to make it illegal is to use broadcasting so it can expand the scalar to match the given matrix's dimensions
grades_with_bonus=grades+5
print('\nGrades after Bonus 5: \n', grades_with_bonus)
#Step8: Normalization
#Since Normalization=(each element-minimum element)/(max -min), therefore:
#minimum element in grades matrix
minimum_grade=np.min(grades)
#maximum element in grades matrix
maximum_grade=np.max(grades)
#By broadcasting: normalized matrix:
normalized_grades=(grades-minimum_grade)/(maximum_grade-minimum_grade)
#By rounding for convenience:
print('\n normalized grades(rounded to 4 decimals): \n', np.round(normalized_grades, 4))
#Purpose of normalization (as far as my knowledge): machine learning algorithms works better when the data is on the same scale, therefore the training data can achieve faster results and higher accuracy
#Flatening the grades into a single vector:
flattened_grades=grades.flatten()
print('\nflattened grades: \n',flattened_grades)



