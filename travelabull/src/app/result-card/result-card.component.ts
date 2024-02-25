// result-card.component.ts

import { Component, Input, OnInit } from '@angular/core';
import { DomSanitizer, SafeResourceUrl } from '@angular/platform-browser';

@Component({
  selector: 'app-result-card',
  templateUrl: './result-card.component.html',
  styleUrls: ['./result-card.component.css']
})
export class ResultCardComponent implements OnInit {
  @Input() result: any; // Use an appropriate type for your result data
  safeMapEmbedUrl!: SafeResourceUrl;

  constructor(private sanitizer: DomSanitizer) {}

  ngOnInit() {
    // Sanitize the Google Maps embed URL
    this.safeMapEmbedUrl = this.sanitizer.bypassSecurityTrustResourceUrl(this.result.mapEmbedLink);
  }
}
