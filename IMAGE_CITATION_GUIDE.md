# Image Citation Guide

This guide explains how to properly cite images and other visual content in your repository.

## Where to Place Images

### Option 1: Concept-Specific Images (Recommended)
Place images in a subdirectory within the concept folder:
```
concepts/evaluation/bias_variance/images/
concepts/preprocessing/normalization/images/
```

**Pros**: Images are co-located with their documentation
**Use when**: Images are specific to one concept

### Option 2: Centralized Images Directory
Place all images in a central location:
```
images/
  ├── concepts/
  │   ├── evaluation/
  │   │   └── bias_variance_tradeoff.png
  │   └── preprocessing/
  └── models/
```

**Pros**: All images in one place, easier to manage
**Use when**: You have many images or want centralized management

## File Naming Convention

Use descriptive, lowercase names with underscores:
- ✅ `bias_variance_tradeoff.png`
- ✅ `normalization_comparison.png`
- ✅ `gradient_descent_visualization.png`
- ❌ `image1.png` (not descriptive)
- ❌ `Bias-Variance.png` (avoid hyphens, use underscores)

## How to Reference Images in Markdown

### Basic Syntax
```markdown
![Alt text](images/filename.png)
```

### With Caption
```markdown
![Bias-Variance Tradeoff](images/bias_variance_tradeoff.png)

*Figure 1: Visual representation of the bias-variance tradeoff.*
```

### Relative Paths
- From README in concept folder: `images/filename.png`
- From root README: `concepts/evaluation/bias_variance/images/filename.png`

## How to Cite Sources

### Format 1: Inline Citation
```markdown
![Bias-Variance Tradeoff](images/bias_variance_tradeoff.png)

*Source: Author Name (Year). Title. [License]*
```

### Format 2: References Section
Add to the References section at the bottom:

```markdown
## References

- Understanding the bias-variance decomposition
- Model complexity and generalization

## Image Credits

- **Bias-Variance Tradeoff Diagram**: Author Name (Year). "Title". 
  Available at: [URL]. Licensed under [License].
```

### Format 3: Detailed Citation
```markdown
## Image Credits

- **Bias-Variance Tradeoff Diagram**: 
  - Author: [Author Name]
  - Year: [Year]
  - Source: [Publication/Website Name]
  - URL: [https://example.com/image]
  - License: [CC BY 4.0 / MIT / etc.]
  - Retrieved: [Date if applicable]
```

## Common License Types

- **CC BY 4.0**: Creative Commons Attribution (most permissive)
- **CC BY-SA 4.0**: Creative Commons Attribution-ShareAlike
- **CC BY-NC 4.0**: Creative Commons Attribution-NonCommercial
- **Public Domain**: No restrictions
- **Fair Use**: Educational use (check local laws)
- **Custom**: Specify terms

## Example Citations

### Academic Paper
```markdown
- **Bias-Variance Tradeoff**: Hastie, T., Tibshirani, R., & Friedman, J. (2009). 
  "The Elements of Statistical Learning" (2nd ed., p. 223). Springer.
```

### Website/Blog
```markdown
- **Bias-Variance Tradeoff**: Smith, J. (2020). "Understanding ML Concepts". 
  Towards Data Science. Available at: https://example.com/article. 
  Licensed under CC BY 4.0.
```

### Your Own Creation
```markdown
- **Bias-Variance Tradeoff**: Created by [Your Name] (2024). 
  Original work.
```

### Modified/Created from Source
```markdown
- **Bias-Variance Tradeoff**: Adapted from Hastie et al. (2009) by [Your Name] (2024). 
  Original source: "The Elements of Statistical Learning".
```

## Best Practices

1. **Always cite**: Even if it's your own work, note it
2. **Be specific**: Include author, year, source, URL
3. **Check licenses**: Ensure you have permission to use the image
4. **Use consistent format**: Pick one citation style and stick to it
5. **Keep it accessible**: Use descriptive alt text for screen readers
6. **Optimize images**: Compress large images before committing

## Legal Considerations

- **Copyright**: Always respect copyright laws
- **Fair Use**: Educational use may be allowed, but check local laws
- **Open Licenses**: Prefer images with open licenses (CC BY, Public Domain)
- **Attribution**: Always provide proper attribution as required by license
- **When in doubt**: Ask permission or create your own

## Tools for Finding Images

- **Unsplash**: Free high-quality photos (check license)
- **Pexels**: Free stock photos (check license)
- **Wikimedia Commons**: Images with clear licensing
- **Create your own**: Use tools like matplotlib, draw.io, or Canva

## Checklist

Before adding an image:
- [ ] Image is placed in appropriate directory
- [ ] File name is descriptive and follows convention
- [ ] Image is referenced correctly in markdown
- [ ] Source is cited properly
- [ ] License is checked and attribution provided
- [ ] Alt text is descriptive
- [ ] Image is optimized (reasonable file size)
