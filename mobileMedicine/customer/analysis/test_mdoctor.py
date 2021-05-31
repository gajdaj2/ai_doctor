from customer.analysis.mdoctor import MDoctor

m_test = MDoctor()

x, y = m_test.data_analysis('diabetes.csv', [3, 107, 62, 13, 48, 22.9, 0.678, 23])

print("Jest cukrzyca {}, {}".format(x, y))

x, y = m_test.data_analysis('diabetes.csv', [1, 138, 82, 0, 0, 40.1, 0.236, 28])

print("Nie ma cukrzyca {}, {}".format(x, y))

# x, y = m_test.data_analysis('heart.csv', [70, 1, 0, 145, 174, 0, 1, 125, 1, 2.6, 0, 0, 3])

# print("{}, {}".format(x, y))


