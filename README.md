# Real Estate Chatbot

This repository contains the code and resources for a Real Estate Chatbot built using Rasa. The chatbot is designed to assist users in obtaining information about real estate properties, answering queries, and facilitating a seamless interaction.

## Features

- **Property Inquiry:** Users can inquire about available properties, their specifications, and other relevant details.
- **Location Information:** The chatbot provides information about the location of properties, nearby amenities, and neighborhood details.
- **Appointment Scheduling:** Users can schedule appointments for property viewings or consultations.
- **Dynamic Conversations:** The chatbot engages users in dynamic conversations, understanding context and providing personalized responses.
- **Error handling:** The chatbot can handle irrelevent questions when asked.
- **FAQ:** The chatbot is also trained to answer questions that are frequently asked by user related to rental and tenent agreements.
## Installation

Clone the repository:

   ```bash
   git clone https://github.com/yourusername/real-estate-chatbot.git
   cd real-estate-chatbot
   ```
Spacy Installation:
 try installing it normally if it doesnt work use the below :
 ```bash
 pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.3.0/en_core_web_sm-2.3.0.tar.gz --no-deps
   ```
## Configuration

- Adjust the configuration files in the `config/` directory for fine-tuning the behavior of the chatbot.
- Customize the domain file (`domain.yml`) to include specific intents, entities, and responses.

## Usage

Train the Rasa model:

   ```bash
   rasa interactive
   ```
Start the Rasa server:

   ```bash
   rasa run actions
   ```
Enter the below command in another terminal
   ```bash
   rasa shell
   ```
To connect the chatbot to the provided chat widget.
   ```bash
   rasa run --enable-api --cors "*" 
   ```

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- Special thanks to the Rasa community for their contributions and support.

```
