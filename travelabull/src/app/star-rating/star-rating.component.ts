import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-star-rating',
  template: `
    <div class="star-rating">
      <span *ngFor="let star of fullStars" class="star full">
        <i class="fas fa-star"></i>
      </span>
      <span *ngIf="hasHalfStar" class="star half">
        <i class="fas fa-star-half-alt"></i>
      </span>
      <span *ngFor="let star of emptyStars" class="star empty">
        <i class="far fa-star"></i>
      </span>
    </div>
  `,
  styles: [`
    .star-rating {
      font-size: 24px;
      cursor: pointer;
    }
    .star {
      color: #ccc;
      transition: color 0.3s;
      display: inline-block;
    }
    .star.full {
      color: gold;
    }
    .star.half {
      color: gold;
    }
    .star.empty {
      color: #ccc;
    }
  `]
})
export class StarRatingComponent {
  @Input() rating: number;
  @Input() totalStars: number = 5;

  fullStars: number[];
  emptyStars: number[];
  hasHalfStar: boolean = false;

  ngOnInit() {
    const fullStarsCount = Math.floor(this.rating);
    this.fullStars = Array.from({ length: fullStarsCount }, (_, index) => index + 1);
    this.hasHalfStar = this.rating % 1 >= 0.5;
    const emptyStarsCount = this.totalStars - fullStarsCount - (this.hasHalfStar ? 1 : 0);
    this.emptyStars = Array.from({ length: emptyStarsCount }, (_, index) => index + 1 + fullStarsCount + (this.hasHalfStar ? 1 : 0));
  }
}
