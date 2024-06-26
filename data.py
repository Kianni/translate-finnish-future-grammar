# File name: data.py
# Description: This file contains the data about the lands
# Author: Kirill Nikolaev

from land import Land


lands_data = [
    {
        "name": "Morocco",
        "capital": "Rabat",
        "greeting": {"phrase": "سلام[Salam]", "response": "وعليكم السلام[Wa alaikum assalam]"},
        "currency": "Moroccan Dirham"
    },
    {
        "name": "Great Britain",
        "capital": "London",
        "greeting": {"phrase": "Hello, how do you do?", "response": "Hello! I'm just fine!"},
        "currency": "Pound Sterling"
    },
    {
        "name": "France",
        "capital": "Paris",
        "greeting": {"phrase": "Bonjour, comment ça va?", "response": "Ça va bien, merci!"},
        "currency": "Euro"
    },
    {
        "name": "Japan",
        "capital": "Tokyo",
        "greeting": {"phrase": "こんにちは、お元気ですか？[Konnichiwa, ogenki desu ka]", "response": "はい、元気です[Hai, genki desu]"},
        "currency": "Yen"
    },
    {
        "name": "Russia",
        "capital": "Moscow",
        "greeting": {"phrase": "Здравствуйте, как дела? [Zdravstvuyte, kak dela?]", "response": "Хорошо, спасибо [Horosho, spasibo!]"},
        "currency": "Ruble"
    },
    {
        "name": "Finland",
        "capital": "Helsinki",
        "greeting": {"phrase": "Moi, mitä kuuluu?", "response": "Kiitos, hyvää."},
        "currency": "Euro"
    }
]

lands = [Land(**land_data) for land_data in lands_data]
