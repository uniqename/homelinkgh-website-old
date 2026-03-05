# HomeLinkGH Webflow Integration Guide

## Current Setup
- **Website**: https://homelinkgh.com (deployed on Netlify)
- **GitHub Repo**: https://github.com/uniqename/homelinkgh-website.git
- **App Store**: Live on Apple App Store and Google Play Store
- **Current Version**: v4.1.0 (approved by Apple and Google)

## Webflow + Netlify Integration (Zero Downtime)

### Option 1: Webflow Export + Netlify Deploy (RECOMMENDED)

This approach keeps your current Netlify deployment and uses Webflow as a visual editor.

#### Step 1: Set Up Webflow Project
1. Go to [Webflow](https://webflow.com) and create a new account
2. Create a new site project: "HomeLinkGH Website"
3. Choose "Blank Site" template
4. Design your website in Webflow's visual editor

#### Step 2: Import Current Design to Webflow
1. Recreate your current website design in Webflow using the visual editor
2. Key pages to recreate:
   - `index.html` - Main homepage
   - `privacy.html` - Privacy policy
   - `terms.html` - Terms of service
   - `support.html` - Support page
   - `delete-account.html` - Account deletion
   - `account/delete.html` - Account deletion form
   - `privacy/delete-data.html` - Data deletion

#### Step 3: Export from Webflow
1. In Webflow, go to Project Settings > Publishing
2. Click "Export Code"
3. Download the ZIP file containing HTML, CSS, JS, and assets

#### Step 4: Deploy to Netlify (Maintain Current Setup)
1. Extract the Webflow export ZIP file
2. Copy the exported files to your local repository:
   ```bash
   cd /Users/enamegyir/Documents/Projects/homelinkgh-website-deploy

   # Backup current files first
   mkdir backup-$(date +%Y%m%d)
   cp -r *.html *.css backup-$(date +%Y%m%d)/

   # Copy Webflow export (adjust path to your download)
   cp -r ~/Downloads/homelinkgh-webflow-export/* .

   # Ensure critical files are preserved
   cp backup-*/netlify.toml .
   cp backup-*/_headers .
   cp backup-*/_redirects .
   ```

3. Commit and push to GitHub:
   ```bash
   git add .
   git commit -m "Update website with Webflow design

   - Redesigned in Webflow visual editor
   - Exported and deployed to Netlify
   - Maintained all privacy and support pages
   - Preserved Netlify configuration

   🤖 Generated with Claude Code
   Co-Authored-By: Claude <noreply@anthropic.com>"

   git push origin main
   ```

4. Netlify will automatically deploy the changes (continuous deployment is already configured)

#### Step 5: Verify Deployment
1. Check Netlify dashboard: https://app.netlify.com
2. Verify the site is live at https://homelinkgh.com
3. Test all pages and links
4. Verify mobile app deep links still work

### Option 2: Webflow Hosting with Netlify DNS (Alternative)

If you prefer to host directly on Webflow:

1. **In Webflow**:
   - Publish your site to Webflow hosting
   - Go to Project Settings > Hosting
   - Add custom domain: `homelinkgh.com`

2. **Update DNS**:
   - In your domain registrar or Netlify DNS settings
   - Point `homelinkgh.com` A record to Webflow's IP
   - Point `www.homelinkgh.com` CNAME to `proxy-ssl.webflow.com`

3. **Considerations**:
   - You'll lose Netlify's continuous deployment from GitHub
   - Webflow hosting costs extra ($12-36/month depending on plan)
   - Updates must be made in Webflow instead of code

### Option 3: Webflow Design System + Custom Code (Hybrid)

For maximum flexibility:

1. Use Webflow to design components and layouts
2. Export HTML/CSS from Webflow
3. Integrate with your custom code for dynamic features
4. Deploy to Netlify as in Option 1

## Important Files to Preserve

Ensure these files are maintained in any Webflow integration:

```
netlify.toml          # Netlify configuration
_headers              # Security headers
_redirects            # URL redirects and rewrites
logo.png              # App logo
favicon.ico           # Site favicon
account-deletion.html # Required by Apple/Google
privacy.html          # Required by Apple/Google
terms.html            # Required by Apple/Google
support.html          # Required by Apple/Google
```

## App Store Requirements

Both Apple and Google require these specific pages for app approval:
- Privacy Policy: https://homelinkgh.com/privacy.html
- Terms of Service: https://homelinkgh.com/terms.html
- Support/Contact: https://homelinkgh.com/support.html
- Account Deletion: https://homelinkgh.com/delete-account.html

**DO NOT change these URLs** without updating the app stores first.

## Continuous Deployment Workflow

With Webflow + Netlify setup:

1. **Design Changes**: Make in Webflow visual editor
2. **Export**: Download code from Webflow
3. **Deploy**: Push to GitHub → Netlify auto-deploys
4. **Verify**: Check live site

## Testing Checklist

After any Webflow integration:
- [ ] Homepage loads correctly
- [ ] All navigation links work
- [ ] Privacy policy accessible
- [ ] Terms of service accessible
- [ ] Support page accessible
- [ ] Account deletion page accessible
- [ ] Mobile responsive design works
- [ ] Forms submit correctly
- [ ] App deep links function (if applicable)
- [ ] SSL certificate valid (HTTPS)
- [ ] Page load speed acceptable

## Rollback Plan

If issues arise:

```bash
cd /Users/enamegyir/Documents/Projects/homelinkgh-website-deploy
git log --oneline  # Find previous commit
git revert HEAD    # Or git reset --hard <commit-hash>
git push origin main
```

Netlify will automatically deploy the previous version.

## Support Resources

- **Webflow University**: https://university.webflow.com
- **Webflow Export Guide**: https://university.webflow.com/lesson/code-export
- **Netlify Docs**: https://docs.netlify.com
- **GitHub Pages**: Your repos at https://github.com/uniqename

## Cost Breakdown

- **Webflow**: $14-35/month (for visual editor and export features)
- **Netlify**: FREE (current setup, includes SSL and CDN)
- **Domain**: ~$12/year (already owned)
- **GitHub**: FREE (current plan)

**Recommended**: Use Webflow's Site Plan ($14/month) for visual editing + Netlify hosting (FREE) for best value.

## Next Steps

1. Sign up for Webflow account
2. Create new project for HomeLinkGH
3. Design in Webflow visual editor
4. Export code
5. Deploy to Netlify via GitHub
6. Test thoroughly
7. Monitor analytics and performance

---

**Created**: October 2025
**App Version**: v4.1.0 (Live on App Store and Google Play)
**Website**: https://homelinkgh.com
