je.epsal-page {
  padding: 16px 18px;
  background: #f6f8f7;
  min-height: 100%;
  font-family: Roboto, Arial, sans-serif;
}

.top-toolbar {
  background: #5e6c75;
  border-radius: 2px;
  padding: 8px 12px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  gap: 16px;
}

.toolbar-left,
.toolbar-right {
  display: flex;
  align-items: center;
  gap: 8px;
}

.section-title {
  margin: 14px 0 10px;
  font-size: 13px;
  font-weight: 500;
  color: #5d9f8c;
}

.epsal-tabs {
  margin-bottom: 14px;
}

.grid-toolbar {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 8px;
}

.grid-actions {
  display: flex;
  align-items: flex-start;
  gap: 10px;
}

.grid-wrapper {
  background: #fff;
  border: 1px solid #dfe5e8;
  padding: 0;
}

.epsal-grid {
  width: 100%;
  height: 420px;
}

:host ::ng-deep .top-toolbar .mat-mdc-text-field-wrapper {
  background: #fff;
  height: 36px;
  border-radius: 2px;
}

:host ::ng-deep .top-toolbar .mdc-notched-outline__leading,
:host ::ng-deep .top-toolbar .mdc-notched-outline__notch,
:host ::ng-deep .top-toolbar .mdc-notched-outline__trailing {
  border-color: #cfd6db !important;
}

:host ::ng-deep .mat-mdc-form-field-subscript-wrapper {
  display: none;
}

:host ::ng-deep .epsal-tabs .mdc-tab {
  min-width: auto;
  height: 34px;
  padding: 0 16px;
  border: 1px solid #95b7ad;
  margin-right: 6px;
  background: #fff;
}

:host ::ng-deep .epsal-tabs .mdc-tab--active {
  background: #7fae9f;
}

:host ::ng-deep .epsal-tabs .mdc-tab--active .mdc-tab__text-label {
  color: #fff !important;
}

:host ::ng-deep .epsal-tabs .mdc-tab__text-label {
  font-size: 12px;
  color: #5f6b6f;
}

.ok-btn {
  min-width: 34px;
  height: 34px;
  padding: 0 10px;
  background: #adcdb7 !important;
  color: #fff !important;
  border-radius: 4px;
  font-size: 12px;
  line-height: 34px;
}

.export-btn {
  height: 36px;
  border-color: #cfd8df !important;
  color: #8390a0 !important;
  background: #fff;
  font-size: 12px;
}

