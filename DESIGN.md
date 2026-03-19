# Design System Specification: High-End Editorial Beauty Management

## 1. Overview & Creative North Star
**Creative North Star: "The Digital Concierge"**
This design system moves away from the "software" aesthetic and toward a "luxury editorial" experience. It is designed for the beauty industry—an environment defined by tactility, elegance, and premium service. 

To break the "template" look, we reject the rigid grid in favor of **intentional asymmetry and tonal depth**. Instead of boxing content into traditional cards, we treat the UI as a series of layered, premium surfaces. By utilizing high-contrast typography scales and generous white space (breathing room), we create an interface that feels less like a tool and more like a high-end portfolio.

---

## 2. Colors & Surface Philosophy
The palette is rooted in a "Noir" foundation, using deep charcoal and matte black to allow white elements and gold accents to radiate.

### Surface Hierarchy & Nesting
We do not use borders to define space. We use **Tonal Layering**.
- **Base Layer:** `surface` (#131313) for the primary application background.
- **Sectioning:** Use `surface_container_low` (#1C1B1B) to define large functional areas.
- **Interactive Layers:** Use `surface_container_high` (#2A2A2A) for floating elements or nested modules.
- **The "No-Line" Rule:** 1px solid borders are strictly prohibited for sectioning. Boundaries must be defined solely through background color shifts or the `surface_container` tiers.

### The "Glass & Gradient" Rule
To add "soul" to the dark matte aesthetic:
- **Glassmorphism:** For floating navigation or modal overlays, use `surface_variant` (#353534) at 60% opacity with a `20px` backdrop-blur. 
- **Signature Accents:** Use `secondary` (#E9C349 - Soft Gold) sparingly. It should appear as a "light catch" on a dial, a notification dot, or a subtle linear gradient (from `secondary` to `secondary_container`) on a high-value CTA.

---

## 3. Typography: The Editorial Voice
The typography is the "scent" of the brand—sophisticated and airy. We pair the geometric strength of **Manrope** for headlines with the clinical clarity of **Inter** for data.

- **Display & Headlines (Manrope):** Use `Light (300)` weight for all `display-lg` through `headline-sm`. The extreme size difference between headlines and body text creates the "Editorial" feel.
- **Body & Labels (Inter):** Use `Regular (400)` or `Light (300)`. Avoid `Bold` weights unless indicating a critical state; instead, use `on_surface_variant` (#C6C6C6) to create hierarchy through color rather than weight.
- **Tracking:** Increase letter-spacing by `0.05em` for all `label` and `title` styles to enhance the "luxury" breathing room.

---

## 4. Elevation & Depth
Depth in this system is perceived, not forced.

- **The Layering Principle:** Place a `surface_container_lowest` (#0E0E0E) element inside a `surface_container` (#201F1F) area to create a "recessed" look, perfect for input fields or data logs.
- **Ambient Shadows:** For "floating" elements like pill-shaped action menus, use a shadow with a blur of `40px` at 8% opacity, using the `on_background` color as the shadow tint.
- **The "Ghost Border" Fallback:** If accessibility requires a container boundary, use the `outline_variant` (#474747) at **15% opacity**. It should be felt, not seen.

---

## 5. Components & Primitives

### Buttons (The Signature Pill)
The button is the most recognizable element of this system.
- **Primary:** Background: `primary` (#FFFFFF), Text: `on_primary` (#1A1C1C). Shape: `full` (9999px). 
- **Secondary:** Background: `transparent`, Border: `outline_variant` (20% opacity), Text: `primary`.
- **Tertiary:** Background: `transparent`, Text: `secondary` (#E9C349). No container.

### Cards & Lists
- **Rule:** Forbid the use of divider lines. 
- **Execution:** Use `spacing-8` (2.75rem) to separate list items vertically. For cards, use a subtle shift from `surface` to `surface_container_low`.

### Inputs & Fields
- **Styling:** Instead of a box, use a "recessed" pill. 
- **Values:** Background: `surface_container_lowest`, Corners: `full` (9999px), Text: `on_surface`.
- **Error State:** Use `error` (#FFB4AB) only for the helper text and a 1px `error` "Ghost Border" (20% opacity).

### Specialized Beauty Components
- **The "Availability Micro-Grid":** A calendar view using `surface_container_highest` for "booked" slots and a `secondary` (Gold) dot for the current selection.
- **Service Chips:** Selection chips should use `md` (1.5rem) roundedness. When selected, they transition from `surface_container_high` to `primary` (White) with `on_primary` text.

---

## 6. Do’s and Don’ts

### Do:
- **Use Excessive White Space:** If you think there is enough space, add one more level of the Spacing Scale (`spacing-10` or `12`).
- **Align to the Optical Center:** In pill buttons and headers, ensure icons are optically centered, not just mathematically centered.
- **Mix Weights:** Use `display-lg` in Light (300) next to a `label-md` in Regular (400) for a high-fashion contrast.

### Don’t:
- **Use Pure Black (#000000):** It kills the "Matte" feel. Always use the `surface` tokens.
- **Use Sharp Corners:** Anything interactive must use at least `DEFAULT` (1rem) or `full` roundedness.
- **Use Dividers:** Never use a line to separate content. Use the `spacing` scale to create "Invisible Dividers."
- **Overuse Gold:** The `secondary` color is a highlight, not a primary fill. It is the "jewelry" of the UI, not the "outfit."

---

## 7. Spacing & Rhythm
This system relies on a **loose, rhythmic scale** to convey luxury.
- **Standard Padding:** Use `spacing-6` (2rem) for internal container padding.
- **External Margins:** Use `spacing-16` (5.5rem) for page gutters to create an ultra-wide, spacious feel that mimics a luxury magazine layout.