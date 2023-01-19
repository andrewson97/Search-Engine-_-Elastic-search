import json

# def standard_analyzer(query):
#     q = {
#         "analyzer": "standard",
#         "text": query
#     }
#     return q

def basic_search(query):
    q = {
        "query": {
            "query_string": {
                "query": query
            }
        }
    }
    return q

# def search_with_field(query, field):
#     q = {
#         "query": {
#             "match": {
#                 field: query
#             }
#         }
#     }
#     return q

# def multi_match(query, fields=['பாடல்', 'பாடல்வரிகள்'], operator='or'):
#     q = {
#         "query": {
#             "multi_match": {
#                 "query": query,
#                 "fields": fields,
#                 "operator": operator,
#                 "type": "best_fields"
#             }
#         }
#     }
#     return q

# def agg_multi_match_q(query, fields=['பாடல்', 'பாடல்வரிகள்'], operator='or'):
#     q = {
#         "size": 500,
#         "explain": True,
#         "query": {
#             "multi_match": {
#                 "query": query,
#                 "fields": fields,
#                 "operator": operator,
#                 "type": "best_fields"
#             }
#         },
#         "aggs": {
#             "Movie Filter": {
#                 "terms": {
#                     "field": "திரைப்படம்.keyword",
#                     "size": 10
#                 }
#             },
#             "Lyricist Filter": {
#                 "terms": {
#                     "field": "பாடலாசிரியர்.keyword",
#                     "size": 10
#                 }
#             },
#             "Year Filter": {
#                 "terms": {
#                     "field": "வருடம்.keyword",
#                     "size": 10
#                 }
#             },
#             "Feel Filter": {
#                 "terms": {
#                     "field": "உணர்வு.keyword",
#                     "size": 10
#                 }
#             },
#             "Tag Filter": {
#                 "terms": {
#                     "field": "குறிச்சொல்.keyword",
#                     "size": 10
#                 }
#             }
#         }
#     }

#     q = json.dumps(q)
#     return q

# def agg_q():
#     q = {
#         "size": 0,
#         "aggs": {
#             "Category Filter": {
#                 "terms": {
#                     "field": "திரைப்படம்",
#                     "size": 10
#                 }
#             }
#         }
#     }

#     return q

