# LLM Distribution - ChatGPT

Skill for getting featured in ChatGPT recommendations.

## Key Facts
- ChatGPT uses **Bing**, not Google
- **No paid placements** - entirely organic
- Entity authority > backlinks
- Listicle mentions > reviews (2:1)

## Prerequisites
- [ ] Bing Merchant Center (required for products)
- [ ] OAI-SearchBot allowed in robots.txt
- [ ] Schema markup: Product, Offer, AggregateRating, Review

## Strategy

### 1. Get Indexed in Bing
- Ensure Bing crawler can access your site
- Submit sitemap to Bing Webmaster Tools
- Don't block OAI-SearchBot in robots.txt

### 2. Build Entity Authority
- Consistent mentions across multiple sources
- Editorial listicles ("Best X for Y")
- Third-party reviews and comparisons
- Reddit/community discussions

### 3. Content Optimization
- Write for conversational queries (avg 23 words)
- Target "Best X for Y" keywords
- Include measurable attributes in descriptions
- Add FAQ schema

### 4. Technical SEO
```json
{
  "@type": "Product",
  "name": "Your Product",
  "description": "...",
  "offers": {
    "@type": "Offer",
    "price": "99.00",
    "priceCurrency": "USD"
  },
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.8",
    "reviewCount": "100"
  }
}
```

## Quick Wins
- Check robots.txt today (2 min)
- Create "Best X for Y" content
- Get listed in 3+ editorial listicles
- Add Product schema to all product pages

## References
- results/llm_distribution/hack_chatgpt.md
