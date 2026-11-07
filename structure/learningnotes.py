
# wend ={1,2,3,4}
# wenderad={1,5,3,6,9}

# diffen=wend.difference(wenderad)
# diff=wenderad-wenderad
# print(diffen)
# print(diff)



# def query_and_document_vector_similarity(query_vector, document_vectors):
#     dot_products = np.dot(
#         document_vectors,
#         query_vector
#     )

#     document_magnitudes = np.linalg.norm(
#         document_vectors,
#         axis=1
#     )
#     query_magnitudes = np.linalg.norm(
#         query_vector
#     )
#     scores = dot_products/(document_magnitudes*query_magnitudes)
#     return scores


# query_vector = np.array([0.8, 0.6])
# document_vector = np.array([
#     [0.9, 0.4],
#     [-0.5, 0.8],
#     [0.7, 0.7]
# ]
# )

# score = query_and_document_vector_similarity(query_vector, document_vector)

# print(score)

# score_rank = np.array([0.72, 0.21, 0.95, 0.44, 0.87])
# indices = np.argsort(score_rank)[::-1]

# top_indices = indices[:3]
# print(indices)
# print(top_indices)
# def cosine_similarity_check(vector_A, vector_B):
#     dot_product = np.dot(vector_A, vector_B)
#     magnitude_of_A = np.linalg.norm(vector_A)
#     magnitude_of_B = np.linalg.norm(vector_B)

#     cosine_similarity = dot_product / (magnitude_of_A*magnitude_of_B)

#     return float(cosine_similarity)


# A = np.array([0.8, 0.6])
# B = np.array([0.7, 0.7])

# result = cosine_similarity_check(A, B)
# print(result)


#     scores = []










# import hashlib

# def group_unique_chunks(chunks):
#     processed_ids=set()
#     document_store={}
#     for chunk in chunks:
#         chunk_id = chunk ["chunk_id "]
#         document_id = chunk ["document_id"]
#         if chunk_id in processed_ids :
#             continue
#         processed_ids.add(chunk_id)
#         if document_id not in document_store :
#             document_store[document_id] = []
#         document_store[document_id] .append(chunk)
#     return document_store

# def generate_content_hash(text):
#     return hashlib.sha256(
#         text.encode("utf-8")
#     ).hexdigest()






# dict = {
#     "name":"okafor"
# }
# dict.get("email")
# dict methods
# #popitem()
# keys()
# values()
# items()
# get()
# update()
# pop()
# copy()
# clear()
# def load_text(fil_path):
#     try:
#         with open(fil_path, "r", encoding="utf-8") as file:

#             content = file.read()
#             if content:
#                 print("document contains text")
#             else:
#                 print("document is empty")
#         return content
#     except FileNotFoundError:
#         print("document does not exist")


# try:
#     with open("C:/Users/s2s/Desktop/des system.txt", "r", encoding="utf-8") as file:
#         content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("document doesnot exist")

# print(type(content))
# print(len(content))

# file = open("C:/Users/s2s/Desktop/design system.txt", "r", encoding="utf-8")

# content = file.read()

# print(content)
# first_line = file.readline()
# second_line = file.readline()

# print(first_line)
# print(second_line)
# lines = file.readlines()
# print(lines)

# file.close()
