# Masterblog

A simple and elegant blogging web application built with Flask. This project demonstrates basic CRUD operations (Create, Read, Update, Delete) with a clean user interface and JSON-based data storage.

## Features

- **View All Posts**: Browse all blog posts on the homepage
- **Create Posts**: Add new blog posts with author, title, and content
- **Update Posts**: Edit existing blog posts
- **Delete Posts**: Remove posts from the blog
- **Like System**: Like your favorite blog posts
- **JSON Storage**: Simple file-based data persistence
- **Responsive UI**: Clean HTML templates with CSS styling

## Tech Stack

- **Python** - Backend programming language
- **Flask** - Web framework
- **HTML/CSS** - Frontend templating and styling
- **JSON** - Data storage

## Project Structure

Masterblog/  
├── app.py # Main Flask application  
├── blog_data.json # Blog posts data storage  
├── requirements.txt # Python dependencies  
├── templates/ # HTML templates  
│ ├── index.html # Homepage displaying all posts  
│ ├── add.html # Form to add new posts  
│ └── update.html # Form to update existing posts  
├── static/ # CSS and static files  
└── LICENSE # MIT License


## Installation

### Prerequisites
- Python 3.7 or higher
- pip

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/Miami05/Masterblog.git
```
```bash
cd Masterblog
```

2. **Install dependencies**
```
pip install -r requirements.txt
```

3. **Run the application**
```
python app.py
```

4. **Open your browser**
Navigate to `http://localhost:5000`

## Usage

### Homepage
The main page displays all blog posts with options to:
- View post details (author, title, content, likes)
- Like posts
- Update posts
- Delete posts
- Add new posts

### Adding a Post
1. Click the "Add Post" button/link on the homepage
2. Fill in the form with:
- Author name
- Post title
- Post content
3. Submit the form to create a new post

### Updating a Post
1. Click the "Update" button on any post
2. Modify the author, title, or content
3. Submit the form to save changes

### Deleting a Post
Click the "Delete" button on any post to permanently remove it

### Liking a Post
Click the "Like" button on any post to increment its like counter

## Data Model

Each blog post has the following structure:

```
{  
"id": 1,  
"author": "John Doe",  
"title": "First Post",  
"content": "This is my first post.",  
"like": 0  
}
```

## Routes

- `GET /` - Homepage displaying all posts
- `GET /add` - Display form to add a new post
- `POST /add` - Submit new post data
- `GET /update/<post_id>` - Display form to update a post
- `POST /update/<post_id>` - Submit updated post data
- `GET /delete/<post_id>` - Delete a specific post
- `GET /like/<post_id>` - Increment like count for a post

## Development

### File Structure
- **app.py**: Contains all Flask routes and application logic
- **blog_data.json**: Stores blog post data in JSON format
- **templates/**: Contains Jinja2 HTML templates
- **static/**: Contains CSS stylesheets and other static assets

### Adding Features
Some ideas for extending this project:
- Add user authentication
- Implement comments on posts
- Add post categories or tags
- Include post timestamps
- Add search functionality
- Implement pagination for posts
- Add rich text editor for content

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Miami05

## Acknowledgments

- Built with Flask web framework
- Simple and educational project for learning web development basics
