import requests


def getAttributesWithProductIds(productIds):
    headers = {
        'Content-Type': 'application/json',
        'authorization': 'Basic dm9ydGEtZHJ1aWQtZHAtdXNlcjpWb3J0YUAxMjM='
    }
    body = {
  "dataSource": {
    "type": "table",
    "name": "mi_product_view_2"
  },
  "context": {
    "queryId": "88624e8d.a28b.4762.bb20.21e729541723aR2jy40Ixl:cl76mtoeb00063b6khwf73nac:5e003a50d0ec4d08950471d882d1f4eb"
  },
  "queryType": "groupBy",
  "intervals": [
    "2022-08-21T05:30:00.000+05:30/2022-08-24T05:29:59.999+05:30"
  ],
  "granularity": "all",
  "filter": {
    "type": "and",
    "fields": [
      {
        "type": "and",
        "fields": [
          {
            "type": "in",
            "dimension": "gender",
            "values": [
              "Men"
            ]
          },
          {
            "type": "in",
            "dimension": "category",
            "values": [
              "Trousers"
            ]
          },
          {
            "type": "in",
            "dimension": "product_id",
            "values": productIds
          }
        ]
      },
      {
        "type": "selector",
        "dimension": "is_live",
        "value": "true"
      }
    ]
  },
  "aggregations": [
    {
      "type": "stringLast",
      "name": "catalog:Trousers:Length",
      "fieldName": "catalog:Trousers:Length"
    },
    {
      "type": "stringLast",
      "name": "catalog:Trousers:Closure",
      "fieldName": "catalog:Trousers:Closure"
    },
    {
      "type": "stringLast",
      "name": "catalog:Trousers:Fit",
      "fieldName": "catalog:Trousers:Fit"
    },
    {
      "type": "stringLast",
      "name": "catalog:Trousers:Print or Pattern Type",
      "fieldName": "catalog:Trousers:Print or Pattern Type"
    },
    {
      "type": "stringLast",
      "name": "catalog:Trousers:Waist Rise",
      "fieldName": "catalog:Trousers:Waist Rise"
    },
    {
      "type": "stringLast",
      "name": "catalog:Trousers:Type",
      "fieldName": "catalog:Trousers:Type"
    }
  ],
  "dimensions": [
    "product_id"
  ]
}
    response = requests.post('https://vdp-druid-router.myntra.com/druid/v2', headers=headers, json=body)
    #print(response.status_code)
    print(response.json())
