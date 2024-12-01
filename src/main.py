import fetch_keywords
import competitor_analysis
import content_optimization
import performance_tracking

if __name__ == "__main__":
    print("Starting Keyword Phrase Optimization Assistant...")
    
    # Fetch existing keyword data
    fetch_keywords.get_keywords_from_search_console()

    # Perform competitor analysis
    competitor_analysis.analyze_competitors()

    # Generate optimization recommendations
    content_optimization.optimize_content()

    # Track performance
    performance_tracking.track_performance()

    print("Reports generated in the 'data/' directory.")
