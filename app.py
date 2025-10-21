from flask import Flask, render_template, request, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'your-secret-key-here-change-in-production'

# Path to articles data file
DATA_FILE = 'data/articles.json'

def load_articles():
    """Load articles from JSON file"""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return []

def save_articles(articles):
    """Save articles to JSON file"""
    os.makedirs('data', exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(articles, f, indent=2)

@app.route('/')
def index():
    """Display all articles"""
    articles = load_articles()
    return render_template('index.html', articles=articles)

@app.route('/article/<int:article_id>')
def article(article_id):
    """Display a specific article"""
    articles = load_articles()
    if 0 <= article_id < len(articles):
        return render_template('article.html', article=articles[article_id], article_id=article_id)
    return "Article not found", 404

@app.route('/add', methods=['GET', 'POST'])
def add_article():
    """Add a new article"""
    if request.method == 'POST':
        articles = load_articles()
        
        # Parse judges from form
        judges = []
        judge_count = int(request.form.get('judge_count', 0))
        for i in range(judge_count):
            judge = {
                'name': request.form.get(f'judge_name_{i}', ''),
                'initials': request.form.get(f'judge_initials_{i}', ''),
                'opinion': request.form.get(f'judge_opinion_{i}', 'yes')
            }
            if judge['name']:
                judges.append(judge)
        
        # Parse timeline items
        timeline = []
        timeline_count = int(request.form.get('timeline_count', 0))
        for i in range(timeline_count):
            item = {
                'title': request.form.get(f'timeline_title_{i}', ''),
                'description': request.form.get(f'timeline_desc_{i}', ''),
                'date': request.form.get(f'timeline_date_{i}', '')
            }
            if item['title']:
                timeline.append(item)
        
        # Parse acts
        acts = []
        acts_input = request.form.get('acts', '')
        if acts_input:
            acts = [act.strip() for act in acts_input.split('\n') if act.strip()]
        
        # Parse citations
        citations = []
        citations_input = request.form.get('citations', '')
        if citations_input:
            citations = [citation.strip() for citation in citations_input.split('\n') if citation.strip()]
        
        # Parse arguments
        petitioner_args = []
        petitioner_args_input = request.form.get('petitioner_arguments', '')
        if petitioner_args_input:
            petitioner_args = [arg.strip() for arg in petitioner_args_input.split('\n') if arg.strip()]
        
        respondent_args = []
        respondent_args_input = request.form.get('respondent_arguments', '')
        if respondent_args_input:
            respondent_args = [arg.strip() for arg in respondent_args_input.split('\n') if arg.strip()]
        
        # Parse verdict points
        verdict_points = []
        verdict_input = request.form.get('verdict_points', '')
        if verdict_input:
            verdict_points = [point.strip() for point in verdict_input.split('\n') if point.strip()]
        
        new_article = {
            'title': request.form.get('title', ''),
            'delivered_date': request.form.get('delivered_date', ''),
            'bench_size': request.form.get('bench_size', ''),
            'intro': request.form.get('intro', ''),
            'plaintiff': request.form.get('plaintiff', ''),
            'defendant': request.form.get('defendant', ''),
            'case_type': request.form.get('case_type', ''),
            'year_range': request.form.get('year_range', ''),
            'judges': judges,
            'ruling': request.form.get('ruling', ''),
            'acts': acts,
            'citations': citations,
            'timeline': timeline,
            'petitioner_arguments': petitioner_args,
            'respondent_arguments': respondent_args,
            'analysis': request.form.get('analysis', ''),
            'verdict_points': verdict_points,
            'ratio_decidendi': request.form.get('ratio_decidendi', ''),
            'case_number': request.form.get('case_number', ''),
            'counsel_petitioner': request.form.get('counsel_petitioner', ''),
            'counsel_respondent': request.form.get('counsel_respondent', ''),
            'hearing_dates': request.form.get('hearing_dates', '')
        }
        
        articles.append(new_article)
        save_articles(articles)
        flash('Article added successfully!', 'success')
        return redirect(url_for('index'))
    
    return render_template('add_article.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
